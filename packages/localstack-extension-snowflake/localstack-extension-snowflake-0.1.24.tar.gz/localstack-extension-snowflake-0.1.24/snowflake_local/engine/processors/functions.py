_B='expressions'
_A='properties'
import re
from localstack.utils.strings import to_bytes
from sqlglot import exp
from snowflake_local.engine.models import Query
from snowflake_local.engine.postgres.db_state import State
from snowflake_local.engine.query_processors import QueryProcessor
from snowflake_local.engine.transform_utils import get_canonical_identifier_multilevel,get_canonical_name
class FixFunctionCodeEscaping(QueryProcessor):
	def transform_query(C,expression,**D):
		A=expression
		if isinstance(A,exp.Create)and str(A.args.get('kind')).upper()=='FUNCTION'and isinstance(A.expression,exp.Literal):B=to_bytes(A.expression.this).decode('unicode_escape');A.expression.args['this']=B
		return A
class LoadJavaScriptFunctionExtension(QueryProcessor):
	def transform_query(F,expression,query,**G):
		A=expression
		if not _is_create_function_or_procedure(A):return A
		C=A.args[_A].expressions;B=[A for A in C if isinstance(A,exp.LanguageProperty)];B=str(B[0].this).lower()if B else None
		if B in('javascript','plv8'):
			D=query.get_database()
			try:from snowflake_local.engine.postgres.db_engine_postgres import install_plv8_extension as E;E();State.server.run_query('CREATE EXTENSION IF NOT EXISTS plv8',database=D)
			except ModuleNotFoundError:pass
		return A
class PrefixRawExpressionWithSelect(QueryProcessor):
	def transform_query(D,expression,**E):
		A=expression;C=exp.Identifier,exp.Cast,exp.Literal
		if not A.parent and isinstance(A,C):B=exp.Select();B.args[_B]=[A];return B
		return A
class RemoveReturnClauseFromProcedures(QueryProcessor):
	def transform_query(C,expression,**D):
		A=expression
		if not _is_create_function_or_procedure(A):return A
		if str(A.args['kind']).upper()!='PROCEDURE':return A
		B=A.args[_A];B.args[_B]=[A for A in B.expressions if not isinstance(A,exp.ReturnsProperty)];return A
class ExtractDbForCallProcedure(QueryProcessor):
	def transform_query(H,expression,query):
		A=expression
		if not isinstance(A,exp.Command)or str(A.this)!='CALL':return A
		E=A.expression.this;B=re.match('\\s*([^(]+)(\\(.+)',str(E))
		if B:
			C=B.group(1);D=C.split('.')
			if len(D)==3:F=get_canonical_name(D[0].strip(),quoted=False);query.database=F.strip('"')
			G=get_canonical_identifier_multilevel(C);A.expression.args['this']=f"{G}{B.group(2)}"
		return A
def _is_create_function_or_procedure(expression):A=expression;return isinstance(A,exp.Create)and isinstance(A.this,exp.UserDefinedFunction)