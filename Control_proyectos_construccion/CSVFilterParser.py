# Generated from CSVFilter.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6-\n\6\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b>\n\b\3\b\3\b")
        buf.write("\3\b\7\bC\n\b\f\b\16\bF\13\b\3\t\3\t\3\t\2\3\16\n\2\4")
        buf.write("\6\b\n\f\16\20\2\3\3\2\17\20\2H\2\23\3\2\2\2\4\33\3\2")
        buf.write("\2\2\6\35\3\2\2\2\b!\3\2\2\2\n&\3\2\2\2\f\60\3\2\2\2\16")
        buf.write("=\3\2\2\2\20G\3\2\2\2\22\24\5\4\3\2\23\22\3\2\2\2\24\25")
        buf.write("\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\3\3\2\2\2\27\34")
        buf.write("\5\6\4\2\30\34\5\b\5\2\31\34\5\n\6\2\32\34\5\f\7\2\33")
        buf.write("\27\3\2\2\2\33\30\3\2\2\2\33\31\3\2\2\2\33\32\3\2\2\2")
        buf.write("\34\5\3\2\2\2\35\36\7\3\2\2\36\37\7\17\2\2\37 \7\4\2\2")
        buf.write(" \7\3\2\2\2!\"\7\5\2\2\"#\7\6\2\2#$\5\16\b\2$%\7\4\2\2")
        buf.write("%\t\3\2\2\2&\'\7\7\2\2\'(\7\f\2\2()\7\6\2\2),\7\17\2\2")
        buf.write("*+\7\b\2\2+-\5\16\b\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./")
        buf.write("\7\4\2\2/\13\3\2\2\2\60\61\7\t\2\2\61\62\7\4\2\2\62\r")
        buf.write("\3\2\2\2\63\64\b\b\1\2\64\65\7\17\2\2\65\66\7\16\2\2\66")
        buf.write(">\5\20\t\2\678\7\17\2\289\7\n\2\29:\5\20\t\2:;\7\13\2")
        buf.write("\2;<\5\20\t\2<>\3\2\2\2=\63\3\2\2\2=\67\3\2\2\2>D\3\2")
        buf.write("\2\2?@\f\5\2\2@A\7\r\2\2AC\5\16\b\6B?\3\2\2\2CF\3\2\2")
        buf.write("\2DB\3\2\2\2DE\3\2\2\2E\17\3\2\2\2FD\3\2\2\2GH\t\2\2\2")
        buf.write("H\21\3\2\2\2\7\25\33,=D")
        return buf.getvalue()


class CSVFilterParser ( Parser ):

    grammarFileName = "CSVFilter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'where'", "'print'", "'BETWEEN'", "'AND'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNC_NAME", "LOGICAL_OP", 
                      "OPERATOR", "STRING", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_loadStat = 2
    RULE_filterStat = 3
    RULE_aggregateStat = 4
    RULE_printStat = 5
    RULE_expr = 6
    RULE_value = 7

    ruleNames =  [ "prog", "stat", "loadStat", "filterStat", "aggregateStat", 
                   "printStat", "expr", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    FUNC_NAME=10
    LOGICAL_OP=11
    OPERATOR=12
    STRING=13
    NUMBER=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.StatContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.StatContext,i)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CSVFilterParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stat()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSVFilterParser.T__0) | (1 << CSVFilterParser.T__2) | (1 << CSVFilterParser.T__4) | (1 << CSVFilterParser.T__6))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStat(self):
            return self.getTypedRuleContext(CSVFilterParser.LoadStatContext,0)


        def filterStat(self):
            return self.getTypedRuleContext(CSVFilterParser.FilterStatContext,0)


        def aggregateStat(self):
            return self.getTypedRuleContext(CSVFilterParser.AggregateStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(CSVFilterParser.PrintStatContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = CSVFilterParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSVFilterParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.loadStat()
                pass
            elif token in [CSVFilterParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.filterStat()
                pass
            elif token in [CSVFilterParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.aggregateStat()
                pass
            elif token in [CSVFilterParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 24
                self.printStat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_loadStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStat" ):
                listener.enterLoadStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStat" ):
                listener.exitLoadStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStat" ):
                return visitor.visitLoadStat(self)
            else:
                return visitor.visitChildren(self)




    def loadStat(self):

        localctx = CSVFilterParser.LoadStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(CSVFilterParser.T__0)
            self.state = 28
            self.match(CSVFilterParser.STRING)
            self.state = 29
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSVFilterParser.ExprContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_filterStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStat" ):
                listener.enterFilterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStat" ):
                listener.exitFilterStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStat" ):
                return visitor.visitFilterStat(self)
            else:
                return visitor.visitChildren(self)




    def filterStat(self):

        localctx = CSVFilterParser.FilterStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CSVFilterParser.T__2)
            self.state = 32
            self.match(CSVFilterParser.T__3)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_NAME(self):
            return self.getToken(CSVFilterParser.FUNC_NAME, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def expr(self):
            return self.getTypedRuleContext(CSVFilterParser.ExprContext,0)


        def getRuleIndex(self):
            return CSVFilterParser.RULE_aggregateStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStat" ):
                listener.enterAggregateStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStat" ):
                listener.exitAggregateStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStat" ):
                return visitor.visitAggregateStat(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStat(self):

        localctx = CSVFilterParser.AggregateStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(CSVFilterParser.T__4)
            self.state = 37
            self.match(CSVFilterParser.FUNC_NAME)
            self.state = 38
            self.match(CSVFilterParser.T__3)
            self.state = 39
            self.match(CSVFilterParser.STRING)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSVFilterParser.T__5:
                self.state = 40
                self.match(CSVFilterParser.T__5)
                self.state = 41
                self.expr(0)


            self.state = 44
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = CSVFilterParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CSVFilterParser.T__6)
            self.state = 47
            self.match(CSVFilterParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSVFilterParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LogicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ExprContext,i)

        def LOGICAL_OP(self):
            return self.getToken(CSVFilterParser.LOGICAL_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)
        def OPERATOR(self):
            return self.getToken(CSVFilterParser.OPERATOR, 0)
        def value(self):
            return self.getTypedRuleContext(CSVFilterParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class BetweenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CSVFilterParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)
        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVFilterParser.ValueContext)
            else:
                return self.getTypedRuleContext(CSVFilterParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenExpr" ):
                listener.enterBetweenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenExpr" ):
                listener.exitBetweenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenExpr" ):
                return visitor.visitBetweenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSVFilterParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CSVFilterParser.ComparisonExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                self.match(CSVFilterParser.STRING)
                self.state = 51
                self.match(CSVFilterParser.OPERATOR)
                self.state = 52
                self.value()
                pass

            elif la_ == 2:
                localctx = CSVFilterParser.BetweenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(CSVFilterParser.STRING)
                self.state = 54
                self.match(CSVFilterParser.T__7)
                self.state = 55
                self.value()
                self.state = 56
                self.match(CSVFilterParser.T__8)
                self.state = 57
                self.value()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSVFilterParser.LogicalExprContext(self, CSVFilterParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 61
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 62
                    self.match(CSVFilterParser.LOGICAL_OP)
                    self.state = 63
                    self.expr(4) 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CSVFilterParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(CSVFilterParser.STRING, 0)

        def getRuleIndex(self):
            return CSVFilterParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = CSVFilterParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not(_la==CSVFilterParser.STRING or _la==CSVFilterParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




