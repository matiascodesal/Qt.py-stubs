# This Python file uses the following encoding: utf-8
#############################################################################
##
## Copyright (C) 2020 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of Qt for Python.
##
## $QT_BEGIN_LICENSE:LGPL$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU Lesser General Public License Usage
## Alternatively, this file may be used under the terms of the GNU Lesser
## General Public License version 3 as published by the Free Software
## Foundation and appearing in the file LICENSE.LGPL3 included in the
## packaging of this file. Please review the following information to
## ensure the GNU Lesser General Public License version 3 requirements
## will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 2.0 or (at your option) the GNU General
## Public license version 3 or any later version approved by the KDE Free
## Qt Foundation. The licenses are as published by the Free Software
## Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-2.0.html and
## https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

"""
This file contains the exact signatures for all functions in module
PySide2.QtScript, except for defaults which are replaced by "...".
"""

# Module PySide2.QtScript
import PySide2
try:
    import typing
except ImportError:
    from PySide2.support.signature import typing
from PySide2.support.signature.mapping import (
    Virtual, Missing, Invalid, Default, Instance)

class Object(object): pass

import shiboken2 as Shiboken
Shiboken.Object = Object

import PySide2.QtCore
import PySide2.QtScript


class QScriptClass(Shiboken.Object):
    Callable                 : QScriptClass = ... # 0x0
    HandlesReadAccess        : QScriptClass = ... # 0x1
    HasInstance              : QScriptClass = ... # 0x1
    HandlesWriteAccess       : QScriptClass = ... # 0x2

    class Extension(object):
        Callable                 : QScriptClass.Extension = ... # 0x0
        HasInstance              : QScriptClass.Extension = ... # 0x1

    class QueryFlag(object):
        HandlesReadAccess        : QScriptClass.QueryFlag = ... # 0x1
        HandlesWriteAccess       : QScriptClass.QueryFlag = ... # 0x2

    def __init__(self, engine:PySide2.QtScript.QScriptEngine): ...

    def engine(self) -> PySide2.QtScript.QScriptEngine: ...
    def extension(self, extension:PySide2.QtScript.QScriptClass.Extension, argument:typing.Any=...) -> typing.Any: ...
    def name(self) -> str: ...
    def newIterator(self, object:PySide2.QtScript.QScriptValue) -> PySide2.QtScript.QScriptClassPropertyIterator: ...
    def property(self, object:PySide2.QtScript.QScriptValue, name:PySide2.QtScript.QScriptString, id:int) -> PySide2.QtScript.QScriptValue: ...
    def propertyFlags(self, object:PySide2.QtScript.QScriptValue, name:PySide2.QtScript.QScriptString, id:int) -> PySide2.QtScript.QScriptValue.PropertyFlags: ...
    def prototype(self) -> PySide2.QtScript.QScriptValue: ...
    def setProperty(self, object:PySide2.QtScript.QScriptValue, name:PySide2.QtScript.QScriptString, id:int, value:PySide2.QtScript.QScriptValue): ...
    def supportsExtension(self, extension:PySide2.QtScript.QScriptClass.Extension) -> bool: ...


class QScriptClassPropertyIterator(Shiboken.Object):

    def __init__(self, object:PySide2.QtScript.QScriptValue): ...

    def flags(self) -> PySide2.QtScript.QScriptValue.PropertyFlags: ...
    def hasNext(self) -> bool: ...
    def hasPrevious(self) -> bool: ...
    def id(self) -> int: ...
    def name(self) -> PySide2.QtScript.QScriptString: ...
    def next(self): ...
    def object(self) -> PySide2.QtScript.QScriptValue: ...
    def previous(self): ...
    def toBack(self): ...
    def toFront(self): ...


class QScriptContext(Shiboken.Object):
    NormalState              : QScriptContext = ... # 0x0
    UnknownError             : QScriptContext = ... # 0x0
    ExceptionState           : QScriptContext = ... # 0x1
    ReferenceError           : QScriptContext = ... # 0x1
    SyntaxError              : QScriptContext = ... # 0x2
    TypeError                : QScriptContext = ... # 0x3
    RangeError               : QScriptContext = ... # 0x4
    URIError                 : QScriptContext = ... # 0x5

    class Error(object):
        UnknownError             : QScriptContext.Error = ... # 0x0
        ReferenceError           : QScriptContext.Error = ... # 0x1
        SyntaxError              : QScriptContext.Error = ... # 0x2
        TypeError                : QScriptContext.Error = ... # 0x3
        RangeError               : QScriptContext.Error = ... # 0x4
        URIError                 : QScriptContext.Error = ... # 0x5

    class ExecutionState(object):
        NormalState              : QScriptContext.ExecutionState = ... # 0x0
        ExceptionState           : QScriptContext.ExecutionState = ... # 0x1
    def activationObject(self) -> PySide2.QtScript.QScriptValue: ...
    def argument(self, index:int) -> PySide2.QtScript.QScriptValue: ...
    def argumentCount(self) -> int: ...
    def argumentsObject(self) -> PySide2.QtScript.QScriptValue: ...
    def backtrace(self) -> typing.List: ...
    def callee(self) -> PySide2.QtScript.QScriptValue: ...
    def engine(self) -> PySide2.QtScript.QScriptEngine: ...
    def isCalledAsConstructor(self) -> bool: ...
    def parentContext(self) -> PySide2.QtScript.QScriptContext: ...
    def popScope(self) -> PySide2.QtScript.QScriptValue: ...
    def pushScope(self, object:PySide2.QtScript.QScriptValue): ...
    def returnValue(self) -> PySide2.QtScript.QScriptValue: ...
    def scopeChain(self) -> typing.List: ...
    def setActivationObject(self, activation:PySide2.QtScript.QScriptValue): ...
    def setReturnValue(self, result:PySide2.QtScript.QScriptValue): ...
    def setThisObject(self, thisObject:PySide2.QtScript.QScriptValue): ...
    def state(self) -> PySide2.QtScript.QScriptContext.ExecutionState: ...
    def thisObject(self) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def throwError(self, error:PySide2.QtScript.QScriptContext.Error, text:str) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def throwError(self, text:str) -> PySide2.QtScript.QScriptValue: ...
    def throwValue(self, value:PySide2.QtScript.QScriptValue) -> PySide2.QtScript.QScriptValue: ...
    def toString(self) -> str: ...


class QScriptContextInfo(Shiboken.Object):
    ScriptFunction           : QScriptContextInfo = ... # 0x0
    QtFunction               : QScriptContextInfo = ... # 0x1
    QtPropertyFunction       : QScriptContextInfo = ... # 0x2
    NativeFunction           : QScriptContextInfo = ... # 0x3

    class FunctionType(object):
        ScriptFunction           : QScriptContextInfo.FunctionType = ... # 0x0
        QtFunction               : QScriptContextInfo.FunctionType = ... # 0x1
        QtPropertyFunction       : QScriptContextInfo.FunctionType = ... # 0x2
        NativeFunction           : QScriptContextInfo.FunctionType = ... # 0x3

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, context:PySide2.QtScript.QScriptContext): ...
    @typing.overload
    def __init__(self, other:PySide2.QtScript.QScriptContextInfo): ...

    def __copy__(self): ...
    def __lshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def __rshift__(self, arg__1:PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream: ...
    def columnNumber(self) -> int: ...
    def fileName(self) -> str: ...
    def functionEndLineNumber(self) -> int: ...
    def functionMetaIndex(self) -> int: ...
    def functionName(self) -> str: ...
    def functionParameterNames(self) -> typing.List: ...
    def functionStartLineNumber(self) -> int: ...
    def functionType(self) -> PySide2.QtScript.QScriptContextInfo.FunctionType: ...
    def isNull(self) -> bool: ...
    def lineNumber(self) -> int: ...
    def scriptId(self) -> int: ...


class QScriptEngine(PySide2.QtCore.QObject):
    QtOwnership              : QScriptEngine = ... # 0x0
    ExcludeChildObjects      : QScriptEngine = ... # 0x1
    ScriptOwnership          : QScriptEngine = ... # 0x1
    AutoOwnership            : QScriptEngine = ... # 0x2
    ExcludeSuperClassMethods : QScriptEngine = ... # 0x2
    ExcludeSuperClassProperties: QScriptEngine = ... # 0x4
    ExcludeSuperClassContents: QScriptEngine = ... # 0x6
    SkipMethodsInEnumeration : QScriptEngine = ... # 0x8
    ExcludeDeleteLater       : QScriptEngine = ... # 0x10
    ExcludeSlots             : QScriptEngine = ... # 0x20
    AutoCreateDynamicProperties: QScriptEngine = ... # 0x100
    PreferExistingWrapperObject: QScriptEngine = ... # 0x200

    class QObjectWrapOption(object):
        ExcludeChildObjects      : QScriptEngine.QObjectWrapOption = ... # 0x1
        ExcludeSuperClassMethods : QScriptEngine.QObjectWrapOption = ... # 0x2
        ExcludeSuperClassProperties: QScriptEngine.QObjectWrapOption = ... # 0x4
        ExcludeSuperClassContents: QScriptEngine.QObjectWrapOption = ... # 0x6
        SkipMethodsInEnumeration : QScriptEngine.QObjectWrapOption = ... # 0x8
        ExcludeDeleteLater       : QScriptEngine.QObjectWrapOption = ... # 0x10
        ExcludeSlots             : QScriptEngine.QObjectWrapOption = ... # 0x20
        AutoCreateDynamicProperties: QScriptEngine.QObjectWrapOption = ... # 0x100
        PreferExistingWrapperObject: QScriptEngine.QObjectWrapOption = ... # 0x200

    class QObjectWrapOptions(object): ...

    class ValueOwnership(object):
        QtOwnership              : QScriptEngine.ValueOwnership = ... # 0x0
        ScriptOwnership          : QScriptEngine.ValueOwnership = ... # 0x1
        AutoOwnership            : QScriptEngine.ValueOwnership = ... # 0x2

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, parent:PySide2.QtCore.QObject): ...

    def abortEvaluation(self, result:PySide2.QtScript.QScriptValue=...): ...
    def agent(self) -> PySide2.QtScript.QScriptEngineAgent: ...
    def availableExtensions(self) -> typing.List: ...
    def canEvaluate(self, program:str) -> bool: ...
    def clearExceptions(self): ...
    def collectGarbage(self): ...
    def currentContext(self) -> PySide2.QtScript.QScriptContext: ...
    def defaultPrototype(self, metaTypeId:int) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def evaluate(self, program:PySide2.QtScript.QScriptProgram) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def evaluate(self, program:str, fileName:str=..., lineNumber:int=...) -> PySide2.QtScript.QScriptValue: ...
    def globalObject(self) -> PySide2.QtScript.QScriptValue: ...
    def hasUncaughtException(self) -> bool: ...
    def importExtension(self, extension:str) -> PySide2.QtScript.QScriptValue: ...
    def importedExtensions(self) -> typing.List: ...
    def installTranslatorFunctions(self, object:PySide2.QtScript.QScriptValue=...): ...
    def isEvaluating(self) -> bool: ...
    def newActivationObject(self) -> PySide2.QtScript.QScriptValue: ...
    def newArray(self, length:int=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newDate(self, value:PySide2.QtCore.QDateTime) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newDate(self, value:float) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newObject(self) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newObject(self, scriptClass:PySide2.QtScript.QScriptClass, data:PySide2.QtScript.QScriptValue=...) -> PySide2.QtScript.QScriptValue: ...
    def newQMetaObject(self, metaObject:PySide2.QtCore.QMetaObject, ctor:PySide2.QtScript.QScriptValue=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newQObject(self, object:PySide2.QtCore.QObject, ownership:PySide2.QtScript.QScriptEngine.ValueOwnership=..., options:PySide2.QtScript.QScriptEngine.QObjectWrapOptions=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newQObject(self, scriptObject:PySide2.QtScript.QScriptValue, qtObject:PySide2.QtCore.QObject, ownership:PySide2.QtScript.QScriptEngine.ValueOwnership=..., options:PySide2.QtScript.QScriptEngine.QObjectWrapOptions=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newRegExp(self, pattern:str, flags:str) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newRegExp(self, regexp:PySide2.QtCore.QRegExp) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newVariant(self, object:PySide2.QtScript.QScriptValue, value:typing.Any) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def newVariant(self, value:typing.Any) -> PySide2.QtScript.QScriptValue: ...
    def nullValue(self) -> PySide2.QtScript.QScriptValue: ...
    def objectById(self, id:int) -> PySide2.QtScript.QScriptValue: ...
    def popContext(self): ...
    def processEventsInterval(self) -> int: ...
    def pushContext(self) -> PySide2.QtScript.QScriptContext: ...
    def reportAdditionalMemoryCost(self, size:int): ...
    def setAgent(self, agent:PySide2.QtScript.QScriptEngineAgent): ...
    def setDefaultPrototype(self, metaTypeId:int, prototype:PySide2.QtScript.QScriptValue): ...
    def setGlobalObject(self, object:PySide2.QtScript.QScriptValue): ...
    def setProcessEventsInterval(self, interval:int): ...
    def toObject(self, value:PySide2.QtScript.QScriptValue) -> PySide2.QtScript.QScriptValue: ...
    def toStringHandle(self, str:str) -> PySide2.QtScript.QScriptString: ...
    def uncaughtException(self) -> PySide2.QtScript.QScriptValue: ...
    def uncaughtExceptionBacktrace(self) -> typing.List: ...
    def uncaughtExceptionLineNumber(self) -> int: ...
    def undefinedValue(self) -> PySide2.QtScript.QScriptValue: ...


class QScriptEngineAgent(Shiboken.Object):
    DebuggerInvocationRequest: QScriptEngineAgent = ... # 0x0

    class Extension(object):
        DebuggerInvocationRequest: QScriptEngineAgent.Extension = ... # 0x0

    def __init__(self, engine:PySide2.QtScript.QScriptEngine): ...

    def contextPop(self): ...
    def contextPush(self): ...
    def engine(self) -> PySide2.QtScript.QScriptEngine: ...
    def exceptionCatch(self, scriptId:int, exception:PySide2.QtScript.QScriptValue): ...
    def exceptionThrow(self, scriptId:int, exception:PySide2.QtScript.QScriptValue, hasHandler:bool): ...
    def extension(self, extension:PySide2.QtScript.QScriptEngineAgent.Extension, argument:typing.Any=...) -> typing.Any: ...
    def functionEntry(self, scriptId:int): ...
    def functionExit(self, scriptId:int, returnValue:PySide2.QtScript.QScriptValue): ...
    def positionChange(self, scriptId:int, lineNumber:int, columnNumber:int): ...
    def scriptLoad(self, id:int, program:str, fileName:str, baseLineNumber:int): ...
    def scriptUnload(self, id:int): ...
    def supportsExtension(self, extension:PySide2.QtScript.QScriptEngineAgent.Extension) -> bool: ...


class QScriptExtensionInterface(PySide2.QtCore.QFactoryInterface):

    def __init__(self): ...

    def initialize(self, key:str, engine:PySide2.QtScript.QScriptEngine): ...


class QScriptExtensionPlugin(PySide2.QtCore.QObject, PySide2.QtScript.QScriptExtensionInterface):

    def __init__(self, parent:typing.Optional[PySide2.QtCore.QObject]=...): ...

    def initialize(self, key:str, engine:PySide2.QtScript.QScriptEngine): ...
    def keys(self) -> typing.List: ...
    def setupPackage(self, key:str, engine:PySide2.QtScript.QScriptEngine) -> PySide2.QtScript.QScriptValue: ...


class QScriptProgram(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtScript.QScriptProgram): ...
    @typing.overload
    def __init__(self, sourceCode:str, fileName:str=..., firstLineNumber:int=...): ...

    def __copy__(self): ...
    def fileName(self) -> str: ...
    def firstLineNumber(self) -> int: ...
    def isNull(self) -> bool: ...
    def sourceCode(self) -> str: ...


class QScriptString(Shiboken.Object):

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, other:PySide2.QtScript.QScriptString): ...

    def __copy__(self): ...
    def isValid(self) -> bool: ...
    def toArrayIndex(self) -> typing.Tuple: ...
    def toString(self) -> str: ...


class QScriptValue(Shiboken.Object):
    UserRange                : QScriptValue = ... # -0x1000000
    NullValue                : QScriptValue = ... # 0x0
    ResolveLocal             : QScriptValue = ... # 0x0
    ReadOnly                 : QScriptValue = ... # 0x1
    ResolvePrototype         : QScriptValue = ... # 0x1
    UndefinedValue           : QScriptValue = ... # 0x1
    ResolveScope             : QScriptValue = ... # 0x2
    Undeletable              : QScriptValue = ... # 0x2
    ResolveFull              : QScriptValue = ... # 0x3
    SkipInEnumeration        : QScriptValue = ... # 0x4
    PropertyGetter           : QScriptValue = ... # 0x8
    PropertySetter           : QScriptValue = ... # 0x10
    QObjectMember            : QScriptValue = ... # 0x20
    KeepExistingFlags        : QScriptValue = ... # 0x800

    class PropertyFlag(object):
        UserRange                : QScriptValue.PropertyFlag = ... # -0x1000000
        ReadOnly                 : QScriptValue.PropertyFlag = ... # 0x1
        Undeletable              : QScriptValue.PropertyFlag = ... # 0x2
        SkipInEnumeration        : QScriptValue.PropertyFlag = ... # 0x4
        PropertyGetter           : QScriptValue.PropertyFlag = ... # 0x8
        PropertySetter           : QScriptValue.PropertyFlag = ... # 0x10
        QObjectMember            : QScriptValue.PropertyFlag = ... # 0x20
        KeepExistingFlags        : QScriptValue.PropertyFlag = ... # 0x800

    class PropertyFlags(object): ...

    class ResolveFlag(object):
        ResolveLocal             : QScriptValue.ResolveFlag = ... # 0x0
        ResolvePrototype         : QScriptValue.ResolveFlag = ... # 0x1
        ResolveScope             : QScriptValue.ResolveFlag = ... # 0x2
        ResolveFull              : QScriptValue.ResolveFlag = ... # 0x3

    class ResolveFlags(object): ...

    class SpecialValue(object):
        NullValue                : QScriptValue.SpecialValue = ... # 0x0
        UndefinedValue           : QScriptValue.SpecialValue = ... # 0x1

    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:PySide2.QtScript.QScriptValue.SpecialValue): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:str): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:bool): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:bytes): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:float): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:int): ...
    @typing.overload
    def __init__(self, engine:PySide2.QtScript.QScriptEngine, val:int): ...
    @typing.overload
    def __init__(self, other:PySide2.QtScript.QScriptValue): ...
    @typing.overload
    def __init__(self, value:PySide2.QtScript.QScriptValue.SpecialValue): ...
    @typing.overload
    def __init__(self, value:str): ...
    @typing.overload
    def __init__(self, value:bool): ...
    @typing.overload
    def __init__(self, value:bytes): ...
    @typing.overload
    def __init__(self, value:float): ...
    @typing.overload
    def __init__(self, value:int): ...
    @typing.overload
    def __init__(self, value:int): ...

    def __copy__(self): ...
    def __iter__(self) -> object: ...
    def __repr__(self) -> object: ...
    @typing.overload
    def call(self, thisObject:PySide2.QtScript.QScriptValue, arguments:PySide2.QtScript.QScriptValue) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def call(self, thisObject:PySide2.QtScript.QScriptValue=..., args:typing.Sequence=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def construct(self, args:typing.Sequence=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def construct(self, arguments:PySide2.QtScript.QScriptValue) -> PySide2.QtScript.QScriptValue: ...
    def data(self) -> PySide2.QtScript.QScriptValue: ...
    def engine(self) -> PySide2.QtScript.QScriptEngine: ...
    def equals(self, other:PySide2.QtScript.QScriptValue) -> bool: ...
    def instanceOf(self, other:PySide2.QtScript.QScriptValue) -> bool: ...
    def isArray(self) -> bool: ...
    def isBool(self) -> bool: ...
    def isBoolean(self) -> bool: ...
    def isDate(self) -> bool: ...
    def isError(self) -> bool: ...
    def isFunction(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isNumber(self) -> bool: ...
    def isObject(self) -> bool: ...
    def isQMetaObject(self) -> bool: ...
    def isQObject(self) -> bool: ...
    def isRegExp(self) -> bool: ...
    def isString(self) -> bool: ...
    def isUndefined(self) -> bool: ...
    def isValid(self) -> bool: ...
    def isVariant(self) -> bool: ...
    def lessThan(self, other:PySide2.QtScript.QScriptValue) -> bool: ...
    def objectId(self) -> int: ...
    @typing.overload
    def property(self, arrayIndex:int, mode:PySide2.QtScript.QScriptValue.ResolveFlags=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def property(self, name:PySide2.QtScript.QScriptString, mode:PySide2.QtScript.QScriptValue.ResolveFlags=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def property(self, name:str, mode:PySide2.QtScript.QScriptValue.ResolveFlags=...) -> PySide2.QtScript.QScriptValue: ...
    @typing.overload
    def propertyFlags(self, name:PySide2.QtScript.QScriptString, mode:PySide2.QtScript.QScriptValue.ResolveFlags=...) -> PySide2.QtScript.QScriptValue.PropertyFlags: ...
    @typing.overload
    def propertyFlags(self, name:str, mode:PySide2.QtScript.QScriptValue.ResolveFlags=...) -> PySide2.QtScript.QScriptValue.PropertyFlags: ...
    def prototype(self) -> PySide2.QtScript.QScriptValue: ...
    def scope(self) -> PySide2.QtScript.QScriptValue: ...
    def scriptClass(self) -> PySide2.QtScript.QScriptClass: ...
    def setData(self, data:PySide2.QtScript.QScriptValue): ...
    @typing.overload
    def setProperty(self, arrayIndex:int, value:PySide2.QtScript.QScriptValue, flags:PySide2.QtScript.QScriptValue.PropertyFlags=...): ...
    @typing.overload
    def setProperty(self, name:PySide2.QtScript.QScriptString, value:PySide2.QtScript.QScriptValue, flags:PySide2.QtScript.QScriptValue.PropertyFlags=...): ...
    @typing.overload
    def setProperty(self, name:str, value:PySide2.QtScript.QScriptValue, flags:PySide2.QtScript.QScriptValue.PropertyFlags=...): ...
    def setPrototype(self, prototype:PySide2.QtScript.QScriptValue): ...
    def setScope(self, scope:PySide2.QtScript.QScriptValue): ...
    def setScriptClass(self, scriptClass:PySide2.QtScript.QScriptClass): ...
    def strictlyEquals(self, other:PySide2.QtScript.QScriptValue) -> bool: ...
    def toBool(self) -> bool: ...
    def toBoolean(self) -> bool: ...
    def toDateTime(self) -> PySide2.QtCore.QDateTime: ...
    def toInt32(self) -> int: ...
    def toInteger(self) -> float: ...
    def toNumber(self) -> float: ...
    def toObject(self) -> PySide2.QtScript.QScriptValue: ...
    def toQMetaObject(self) -> PySide2.QtCore.QMetaObject: ...
    def toQObject(self) -> PySide2.QtCore.QObject: ...
    def toRegExp(self) -> PySide2.QtCore.QRegExp: ...
    def toString(self) -> str: ...
    def toUInt16(self) -> int: ...
    def toUInt32(self) -> int: ...
    def toVariant(self) -> typing.Any: ...


class QScriptValueIterator(Shiboken.Object):

    def __init__(self, value:PySide2.QtScript.QScriptValue): ...

    def __iter__(self) -> object: ...
    def __next__(self) -> object: ...
    def flags(self) -> PySide2.QtScript.QScriptValue.PropertyFlags: ...
    def hasNext(self) -> bool: ...
    def hasPrevious(self) -> bool: ...
    def name(self) -> str: ...
    def next(self): ...
    def previous(self): ...
    def remove(self): ...
    def scriptName(self) -> PySide2.QtScript.QScriptString: ...
    def setValue(self, value:PySide2.QtScript.QScriptValue): ...
    def toBack(self): ...
    def toFront(self): ...
    def value(self) -> PySide2.QtScript.QScriptValue: ...


class QScriptable(Shiboken.Object):

    def __init__(self): ...

    def argument(self, index:int) -> PySide2.QtScript.QScriptValue: ...
    def argumentCount(self) -> int: ...
    def context(self) -> PySide2.QtScript.QScriptContext: ...
    def engine(self) -> PySide2.QtScript.QScriptEngine: ...
    def thisObject(self) -> PySide2.QtScript.QScriptValue: ...

# eof
