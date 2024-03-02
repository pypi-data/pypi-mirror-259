import sys
from typing import Any, Generator, Literal, Optional, TextIO


NodesWithName = tuple[tuple[str, Node], ...]
NodeGenerator = Generator[Node, Node, Node]

TypeQualifier = Literal['const', 'restrict', 'volatile']
StorageSpecifier = Literal['auto', 'register', 'static', 'extern']
FunctionSpecifier = Literal['inline', '_Noreturn']

TypeSpecifier = IdentifierType | Struct | Union | Enum
TypeModifier = ArrayDecl | FuncDecl | PtrDecl
# https://en.cppreference.com/w/c/language/declarations#Declarators
# Note: this is different from real declarators.
Declarator = TypeModifier | TypeDecl

# https://en.cppreference.com/w/c/language/expressions#Primary_expressions
PrimaryExpression = Constant | ID
# https://en.cppreference.com/w/c/language/expressions#Operators
Expression = UnaryOp | BinaryOp | TernaryOp | Assignment | ArrayRef | StructRef \
           | FuncCall | ExprList | Cast | PrimaryExpression

# https://en.cppreference.com/w/c/language/statements#Labels
LabeledStatement = Label | Case | Default
# https://en.cppreference.com/w/c/language/statements#Expression_statements
ExpressionStatement = Expression | EmptyStatement
# https://en.cppreference.com/w/c/language/statements#Selection_statements
SelectionStatement = If | Switch
# https://en.cppreference.com/w/c/language/statements#Iteration_statements
IterationStatement = While | DoWhile | For
# https://en.cppreference.com/w/c/language/statements#Jump_statements
JumpStatement = Break | Continue | Return | Goto
# https://en.cppreference.com/w/c/language/statements
Statement = StaticAssert | Pragma | LabeledStatement | Compound | ExpressionStatement \
          | SelectionStatement | IterationStatement | JumpStatement

# these types ARE NOT GUARANTEED at AST level, just made as a hint
StringLiteral = Constant
IntegerConstantExpression = Expression

FileLevelNode = StaticAssert | Pragma | Decl | FuncDef


class Node(object):
    """ Abstract base class for AST nodes. """
    
    def __repr__(self) -> str: ...
    
    def children(self) -> NodesWithName:
        """ A sequence of all children that are Nodes. """
        ...

    def show(self,
        buf: TextIO = sys.stdout,
        offset: int = 0,
        attrnames: bool = False,
        nodenames: bool = False,
        showcoord: bool = False,
        _my_node_name: Optional[str] = None
    ) -> None:
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

            showcoord:
                Do you want the coordinates of each Node to be
                displayed.
        """
        ...


class NodeVisitor(object):
    """ A base NodeVisitor class for visiting c_ast nodes.
        Subclass it and define your own visit_XXX methods, where
        XXX is the class name you want to visit with these
        methods.

        For example:

        class ConstantVisitor(NodeVisitor):
            def __init__(self):
                self.values = []

            def visit_Constant(self, node):
                self.values.append(node.value)

        Creates a list of values of all the constant nodes
        encountered below the given node. To use it:

        cv = ConstantVisitor()
        cv.visit(node)

        Notes:

        *   generic_visit() will be called for AST nodes for which
            no visit_XXX method was defined.
        *   The children of nodes for which a visit_XXX was
            defined will not be visited - if you need this, call
            generic_visit() on the node.
            You can use:
                NodeVisitor.generic_visit(self, node)
        *   Modeled after Python's own AST visiting facilities
            (the ast module of Python 3.0)
    """

    def visit(self, node: Node) -> Any:
        """ Visit a node.
        """
        ...

    def generic_visit(self, node: Node) -> None:
        """ Called if no explicit visitor function exists for a
            node. Implements preorder visiting of the node.
        """
        ...


class Constant(Node):
    type: str
    value: str
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('type', 'value', )


class ID(Node): # Identifier
    name: str
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class IdentifierType(Node):
    names: list[str]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('names', )


class Alignas(Node):
    alignment: IntegerConstantExpression | Typename
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class UnaryOp(Node):
    op: str
    expr: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('op', )


class BinaryOp(Node):
    op: str
    left: Expression
    right: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('op', )


class TernaryOp(Node):
    cond: Expression
    iftrue: Expression
    iffalse: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Assignment(Node):
    op: str
    lvalue: Expression
    rvalue: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('op', )


class ArrayRef(Node):
    name: Expression
    subscript: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class StructRef(Node):
    name: Expression
    type: str
    field: ID
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('type', )


class FuncCall(Node):
    name: Expression
    args: ExprList
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class ExprList(Node): # CommaExpression
    exprs: list[Expression]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Cast(Node):
    to_type: Typename
    expr: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class NamedInitializer(Node): # DesignatedInitializer
    name: list[ID | IntegerConstantExpression]
    expr: Expression
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class InitList(Node):
    exprs: list[Expression | NamedInitializer]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class CompoundLiteral(Node):
    type: Typename
    init: InitList
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Decl(Node): # Declaration
    name: str
    quals: list[TypeQualifier]
    align: Alignas
    storage: list[StorageSpecifier]
    funcspec: list[FunctionSpecifier]
    type: Declarator
    init: Optional[InitList | Expression]
    bitsize: Optional[IntegerConstantExpression]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', 'quals', 'align', 'storage', 'funcspec', )


class DeclList(Node):
    decls: list[Decl]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Typename(Node):
    name: Optional[str]
    quals: list[TypeQualifier]
    align: Optional[Alignas]
    type: Declarator
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', 'quals', 'align', )


class Typedef(Node):
    name: str
    quals: list[TypeQualifier]
    storage: list[Literal['typedef']]
    type: Declarator
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', 'quals', 'storage', )


class ArrayDecl(Node):
    type: Declarator
    dim: Optional[Expression] # maybe VLA
    dim_quals: list[TypeQualifier]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('dim_quals', )


class EllipsisParam(Node):
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class ParamList(Node):
    params: list[Decl | EllipsisParam]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class FuncDecl(Node):
    args: Optional[ParamList]
    type: Declarator
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class PtrDecl(Node):
    quals: list[TypeQualifier]
    type: Declarator
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('quals', )


class TypeDecl(Node):
    declname: Optional[str]
    quals: list[TypeQualifier]
    align: Optional[Alignas]
    type: TypeSpecifier
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('declname', 'quals', 'align', )


class Struct(Node):
    name: str
    decls: Optional[list[Decl]]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class Union(Node):
    name: str
    decls: Optional[list[Decl]]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class Enumerator(Node):
    name: str
    value: Optional[IntegerConstantExpression]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class EnumeratorList(Node):
    enumerators: list[Enumerator]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Enum(Node):
    name: str
    values: Optional[EnumeratorList]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class StaticAssert(Node):
    cond: IntegerConstantExpression
    message: Optional[StringLiteral]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Pragma(Node):
    string: str
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('string', )


class Label(Node):
    name: str
    stmt: Statement
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class Case(Node):
    expr: IntegerConstantExpression
    stmts: list[Statement]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Default(Node):
    stmts: list[Statement]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Compound(Node): # CompoundStatement
    block_items: Optional[list[Statement | Decl]]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class EmptyStatement(Node):
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class If(Node):
    cond: Expression
    iftrue: Statement
    iffalse: Optional[Statement]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Switch(Node):
    cond: Expression
    stmt: Statement
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class While(Node):
    cond: Expression
    stmt: Statement
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class DoWhile(Node):
    cond: Expression
    stmt: Statement
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class For(Node):
    init: Optional[Expression | DeclList]
    cond: Optional[Expression]
    next: Optional[Expression]
    stmt: Statement
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Break(Node):
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Continue(Node):
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Return(Node):
    expr: Optional[Expression]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class Goto(Node):
    name: ID
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ('name', )


class FuncDef(Node):
    decl: Decl
    param_decls: Optional[list[Decl]]
    body: Compound
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()


class FileAST(Node):
    ext: list[FileLevelNode]
    def children(self) -> NodesWithName: ...
    def __iter__(self) -> NodeGenerator: ...
    attr_names = ()
