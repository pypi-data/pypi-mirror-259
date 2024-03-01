_B='postgres'
_A=False
import gzip,io,json,logging,re
from localstack.utils.files import chmod_r,new_tmp_file,rm_rf,save_file
from localstack.utils.functions import run_safe
from sqlglot import exp,parse_one
from snowflake_local import config
from snowflake_local.engine.models import Query
from snowflake_local.engine.postgres.db_state import State
from snowflake_local.engine.processors.types import TYPE_MAPPINGS
from snowflake_local.engine.query_processors import QueryProcessor
from snowflake_local.engine.session import APP_STATE
from snowflake_local.engine.transform_utils import get_canonical_name,to_variant
from snowflake_local.engine.transforms import apply_query_transforms
from snowflake_local.files.file_ops import _parse_tabular_data,handle_copy_into_query,handle_put_file_query
from snowflake_local.files.storage import FILE_STORAGE,FileRef
from snowflake_local.server.models import QueryResponse
LOG=logging.getLogger(__name__)
class HandleCreateStage(QueryProcessor):
	REGEX=re.compile('CREATE\\s+(OR\\s+REPLACE\\s+)?(TEMP(ORARY)?\\s+)?STAGE\\s+(\\S+)',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def transform_query(C,expression,**E):
		A=expression
		if isinstance(A,exp.Command)and str(A.this).upper()=='CREATE':D=C.REGEX.match(str(A));B=D.group(4).upper();LOG.info("Processing `CREATE STAGE` query to create stage '%s'",B);return parse_one(f"SELECT 'Stage area {B} successfully created.'",read=_B)
		return A
class HandleDropStage(QueryProcessor):
	REGEX=re.compile('DROP\\s+STAGE\\s+(IF\\s+EXISTS\\s+)?(\\S+)',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def transform_query(B,expression,**E):
		A=expression
		if isinstance(A,exp.Command)and str(A.this).upper()=='DROP':C=B.REGEX.match(str(A));D=C.group(2).upper();return parse_one(f"SELECT '{D} successfully dropped.'",read=_B)
		return A
class CreateTmpTableForResultScan(QueryProcessor):
	def transform_query(L,expression,**M):
		G='this';A=expression
		if isinstance(A,exp.Func)and str(A.this).upper()=='RESULT_SCAN':
			E=A.expressions[0];F=E.this;B=APP_STATE.queries.get(F)
			if not B:LOG.info("Unable to find state for query ID '%s'",F);return A
			C=new_tmp_file();H=json.dumps(B.result.rows);save_file(C,H);chmod_r(C,511);E.args[G]=C
			def I(idx,col):B=col;A=B.type_name.upper();A=TYPE_MAPPINGS.get(A)or A;return f"{f'_col{idx+1}'if B.name.lower()=='?column?'else B.name} {A}"
			D=exp.Alias();D.args[G]=A;J=B.result.columns;K=', '.join([I(A,B)for(A,B)in enumerate(J)]);D.args['alias']=f"({K})";return D
		return A
class HandleInferSchema(QueryProcessor):
	def initialize_db_resources(C,database):B=State.server;A=f"""
        CREATE OR REPLACE FUNCTION {get_canonical_name("infer_schema")} (
            location TEXT, file_format TEXT DEFAULT NULL, files TEXT[] DEFAULT NULL,
            ignore_case BOOL DEFAULT FALSE, max_file_count INT DEFAULT NULL, max_records_per_file INT DEFAULT NULL
        ) RETURNS TABLE (
            COLUMN_NAME TEXT, TYPE TEXT, NULLABLE BOOL, EXPRESSION TEXT, FILENAMES TEXT, ORDER_ID INT
        ) LANGUAGE plpython3u IMMUTABLE AS $$
            from snowflake_local.engine.processors.stages import HandleInferSchema
            return HandleInferSchema.infer_schema(
                {get_canonical_name("location",quoted=_A)},
                {get_canonical_name("file_format",quoted=_A)},
                {get_canonical_name("files",quoted=_A)},
                {get_canonical_name("ignore_case",quoted=_A)},
                {get_canonical_name("max_file_count",quoted=_A)},
                {get_canonical_name("max_records_per_file",quoted=_A)})
        $$
        """;A=apply_query_transforms(A);B.run_query(A.query,database=database)
	@classmethod
	def infer_schema(J,_location,_file_format,_files,_ignore_case,_max_files,_max_records_per_file):
		B=None;from pyarrow import parquet as E;F=FileRef.parse(_location);C=[];G=FILE_STORAGE.list_files(F)
		for H in G:
			A=FILE_STORAGE.load_file(H);A=run_safe(lambda:gzip.decompress(A),_default=A)
			if A.startswith(b'PAR1'):
				I=E.read_table(io.BytesIO(A))
				for D in I.schema:C.append({get_canonical_name('column_name',quoted=_A):D.name,get_canonical_name('type',quoted=_A):str(D.type),get_canonical_name('nullable',quoted=_A):True,get_canonical_name('expression',quoted=_A):B,get_canonical_name('filenames',quoted=_A):B,get_canonical_name('order_id',quoted=_A):B})
		return C
class DefineLoadDataFunction(QueryProcessor):
	def initialize_db_resources(C,database):A=State.server;B=f"""
            CREATE OR REPLACE FUNCTION {get_canonical_name("load_data")} (
               file_ref text,
               file_format text
            ) RETURNS SETOF RECORD
            LANGUAGE plpython3u IMMUTABLE AS $$
                from snowflake_local.engine.processors.stages import DefineLoadDataFunction
                return DefineLoadDataFunction.load_data(file_ref, file_format)
            $$
        """;A.run_query(B,database=database)
	@classmethod
	def load_data(I,file_ref,file_format):
		from snowflake_local.files.storage import FILE_STORAGE as C,FileRef as D;E=D.parse(file_ref);F=C.load_file(E);G=_parse_tabular_data(F);A=[]
		for B in G:
			if isinstance(B,dict):H='_COL1'if config.CONVERT_NAME_CASING else'_col1';A.append({H:to_variant(B)})
			else:A.append(B)
		return A
class HandleResultScan(QueryProcessor):
	def initialize_db_resources(B,database):A=f"""
            CREATE OR REPLACE FUNCTION {get_canonical_name("result_scan")}
            (results_file TEXT) RETURNS SETOF RECORD
            LANGUAGE plpython3u IMMUTABLE
            AS $$
                from snowflake_local.engine.processors.stages import HandleResultScan
                return HandleResultScan.result_scan(results_file)
            $$
        """;State.server.run_query(A,database=database)
	@classmethod
	def result_scan(D,file_path):
		A=file_path
		with open(A)as B:C=json.loads(B.read())
		try:rm_rf(A)
		except Exception:pass
		return C
class HandlePutQuery(QueryProcessor):
	REGEX=re.compile('^\\s*PUT\\s+.+',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def transform_query(B,expression,query):
		A=expression
		if isinstance(A,exp.Command)and str(A.this).upper()=='PUT':return parse_one('SELECT NULL')
		return A
	def postprocess_result(C,query,result):A=result;B=handle_put_file_query(query.original_query,A);A.data=B.data
class HandleCopyIntoQuery(QueryProcessor):
	REGEX=re.compile('^\\s*COPY\\s+INTO\\s.+',flags=re.I)
	def should_apply(A,query):return bool(A.REGEX.match(query.original_query))
	def transform_query(B,expression,query):
		A=expression
		if isinstance(A,exp.Command)and str(A.this).upper()=='COPY':return parse_one('SELECT NULL LIMIT 0')
		return A
	def postprocess_result(A,query,result):handle_copy_into_query(query,result)