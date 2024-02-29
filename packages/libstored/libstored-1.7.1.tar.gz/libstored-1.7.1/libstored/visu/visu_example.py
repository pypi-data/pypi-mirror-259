# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x05\xe5\
/\
/ SPDX-FileCopyr\
ightText: 2020-2\
023 Jochem Rutge\
rs\x0a//\x0a// SPDX-Li\
cense-Identifier\
: CC0-1.0\x0a\x0aimpor\
t QtQuick 2.12\x0ai\
mport QtQuick.La\
youts 1.15\x0aimpor\
t QtQuick.Window\
 2.2\x0aimport QtQu\
ick.Controls 2.5\
\x0a\x0aWindow {\x0a\x0a    \
id: root\x0a    vis\
ible: true\x0a    w\
idth: 400\x0a    he\
ight: 300\x0a\x0a    r\
eadonly property\
 int fontSize: 1\
0\x0a\x0a    Component\
.onCompleted: {\x0a\
        var text\
 = \x22Visu\x22\x0a\x0a     \
   var id = clie\
nt.identificatio\
n()\x0a        if(i\
d && id !== \x22?\x22)\
\x0a        {\x0a     \
       text += \x22\
: \x22 + id\x0a\x0a      \
      var v = cl\
ient.version()\x0a \
           if(v \
&& v !== \x22?\x22)\x0a  \
              te\
xt += \x22 (\x22 + v +\
 \x22)\x22\x0a        }\x0a\x0a\
        root.tit\
le = text\x0a    }\x0a\
\x0a    ColumnLayou\
t {\x0a        anch\
ors.fill: parent\
\x0a        anchors\
.margins: 5\x0a\x0a   \
     TextField {\
\x0a            id:\
 req\x0a           \
 Layout.preferre\
dHeight: root.fo\
ntSize * 2\x0a     \
       font.pixe\
lSize: root.font\
Size\x0a           \
 Layout.fillWidt\
h: true\x0a        \
    placeholderT\
ext: \x22enter comm\
and\x22\x0a           \
 background.anti\
aliasing: true\x0a \
           topPa\
dding: 0\x0a       \
     bottomPaddi\
ng: 0\x0a\x0a         \
   onAccepted: {\
\x0a               \
 rep.text = clie\
nt.req(text)\x0a   \
         }\x0a     \
   }\x0a\x0a        Sc\
rollView {\x0a     \
       Layout.fi\
llWidth: true\x0a  \
          Layout\
.fillHeight: tru\
e\x0a            cl\
ip: true\x0a\x0a      \
      TextArea {\
\x0a               \
 id: rep\x0a       \
         readOnl\
y: true\x0a        \
        font.pix\
elSize: root.fon\
tSize\x0a          \
  }\x0a\x0a           \
 background: Rec\
tangle {\x0a       \
         antiali\
asing: true\x0a    \
            bord\
er.color: \x22#c0c0\
c0\x22\x0a            \
}\x0a        }\x0a    \
}\x0a}\x0a\
\x00\x00\x05j\
/\
/ SPDX-FileCopyr\
ightText: 2020-2\
023 Jochem Rutge\
rs\x0a//\x0a// SPDX-Li\
cense-Identifier\
: MPL-2.0\x0a\x0aimpor\
t QtQuick.Contro\
ls\x0aimport QtQuic\
k\x0a\x0aTextField {\x0a \
   id: comp\x0a\x0a   \
 background.anti\
aliasing: true\x0a\x0a\
    topPadding: \
0\x0a    bottomPadd\
ing: 0\x0a    leftP\
adding: 0\x0a    ho\
rizontalAlignmen\
t: TextInput.Ali\
gnRight\x0a    read\
Only: true\x0a\x0a    \
property string \
unit: ''\x0a\x0a    pr\
operty alias ref\
: o.ref\x0a    prop\
erty alias obj: \
o.obj\x0a    proper\
ty alias pollInt\
erval: o.pollInt\
erval\x0a    proper\
ty alias refresh\
ed: o.refreshed\x0a\
    property ali\
as value: o.valu\
e\x0a    property b\
ool connected: o\
.obj !== null\x0a  \
  property alias\
 autoReadOnInit:\
 o.autoReadOnIni\
t\x0a\x0a    property \
var o: StoreObje\
ct {\x0a        id:\
 o\x0a    }\x0a\x0a    //\
 Specify a (lamb\
da) function, wh\
ich will be used\
 to convert the \
value\x0a    // to \
a string. If nul\
l, the valueStri\
ng of the object\
 is used.\x0a    pr\
operty var forma\
tter: null\x0a\x0a    \
property string \
valueFormatted: \
{\x0a        var s;\
\x0a\x0a        if(!co\
nnected)\x0a       \
     s = '';\x0a   \
     else if(for\
matter)\x0a        \
    s = formatte\
r(o.value);\x0a    \
    else\x0a       \
     s = o.value\
String;\x0a\x0a       \
 return s\x0a    }\x0a\
\x0a    property st\
ring _text: {\x0a  \
      var s = ''\
;\x0a        if(!co\
nnected)\x0a       \
     s = '?';\x0a  \
      else\x0a     \
       s = value\
Formatted;\x0a\x0a    \
    if(unit != '\
')\x0a            s\
 += ' ' + unit\x0a\x0a\
        return s\
\x0a    }\x0a    text:\
 _text\x0a\x0a    colo\
r: !connected ? \
\x22gray\x22 : refresh\
ed ? \x22blue\x22 : \x22b\
lack\x22\x0a}\x0a\x0a\
\x00\x00\x05\x87\
/\
/ SPDX-FileCopyr\
ightText: 2020-2\
023 Jochem Rutge\
rs\x0a//\x0a// SPDX-Li\
cense-Identifier\
: MPL-2.0\x0a\x0aimpor\
t QtQuick.Contro\
ls\x0aimport QtQuic\
k\x0a\x0aMeasurement {\
\x0a    readOnly: f\
alse\x0a    pollInt\
erval: 0\x0a\x0a    pr\
operty bool edit\
ing: activeFocus\
 && displayText \
!= valueFormatte\
d\x0a\x0a    property \
bool _edited: fa\
lse\x0a    onEditin\
gChanged : {\x0a   \
     if(!editing\
) {\x0a            \
_edited = true\x0a \
           Qt.ca\
llLater(function\
() { _edited: fa\
lse })\x0a        }\
\x0a    }\x0a\x0a    prop\
erty bool valid:\
 true\x0a    proper\
ty color validBa\
ckgroundColor: \x22\
white\x22\x0a    prope\
rty color invali\
dBackgroundColor\
: \x22#ffe0e0\x22\x0a    \
palette.base: va\
lid ? validBackg\
roundColor : inv\
alidBackgroundCo\
lor\x0a\x0a    color: \
editing ? \x22red\x22 \
: !connected ? \x22\
gray\x22 : refreshe\
d && !_edited ? \
\x22blue\x22 : \x22black\x22\
\x0a    text: \x22\x22\x0a\x0a \
   onAccepted: {\
\x0a        o.set(d\
isplayText)\x0a    \
    Qt.callLater\
(function() { te\
xt = valueFormat\
ted })\x0a    }\x0a\x0a  \
  onActiveFocusC\
hanged: {\x0a      \
  if(activeFocus\
)\x0a            te\
xt = valueFormat\
ted\x0a        else\
\x0a            tex\
t = _text\x0a    }\x0a\
\x0a    on_TextChan\
ged: {\x0a        i\
f(!editing)\x0a    \
        text = _\
text\x0a    }\x0a\x0a    \
Keys.forwardTo: \
decimalPointConv\
ersion\x0a    Item \
{\x0a        id: de\
cimalPointConver\
sion\x0a        Key\
s.onPressed: (ev\
ent) => {\x0a      \
      if(obj !==\
 null && event.k\
ey == Qt.Key_Per\
iod && (event.mo\
difiers & Qt.Key\
padModifier)) {\x0a\
                \
event.accepted =\
 true\x0a          \
      obj.inject\
DecimalPoint(par\
ent)\x0a           \
 }\x0a        }\x0a   \
 }\x0a}\x0a\x0a\
\x00\x00\x00\xc9\
#\
 SPDX-FileCopyri\
ghtText: 2020-20\
23 Jochem Rutger\
s\x0a#\x0a# SPDX-Licen\
se-Identifier: C\
C0-1.0\x0a\x0amodule L\
ibstored.Compone\
nts\x0aInput 1.0 In\
put.qml\x0aMeasurem\
ent 1.0 Measurem\
ent.qml\x0aStoreObj\
ect 1.0 StoreObj\
ect.qml\x0a\
\x00\x00\x05\xe4\
/\
/ SPDX-FileCopyr\
ightText: 2020-2\
023 Jochem Rutge\
rs\x0a//\x0a// SPDX-Li\
cense-Identifier\
: MPL-2.0\x0a\x0aimpor\
t QtQuick\x0a\x0aItem \
{\x0a    id: comp\x0a\x0a\
    required pro\
perty var ref\x0a  \
  property var o\
bj: null\x0a    pro\
perty string nam\
e: obj ? obj.nam\
e : \x22\x22\x0a    prope\
rty real pollInt\
erval: 2\x0a    pro\
perty bool autoR\
eadOnInit: true\x0a\
\x0a    onRefChange\
d: {\x0a        if(\
typeof(ref) != \x22\
string\x22) {\x0a     \
       obj = ref\
\x0a        } else \
if(typeof(client\
) == \x22undefined\x22\
) {\x0a            \
obj = null\x0a     \
   } else {\x0a    \
        obj = cl\
ient.obj(ref)\x0a  \
      }\x0a    }\x0a\x0a \
   onObjChanged:\
 {\x0a        if(ob\
j) {\x0a           \
 value = obj.val\
ueSafe\x0a\x0a        \
    if(!obj.poll\
ing) {\x0a         \
       if(pollIn\
terval > 0)\x0a    \
                \
obj.poll(pollInt\
erval)\x0a         \
       else if(a\
utoReadOnInit)\x0a \
                \
   obj.asyncRead\
()\x0a            }\
 else if(pollInt\
erval > 0 && obj\
.pollInterval > \
pollInterval) {\x0a\
                \
// Prefer the fa\
ster setting, if\
 there are multi\
ple.\x0a           \
     obj.poll(po\
llInterval)\x0a    \
        }\x0a      \
  } else {\x0a     \
       value = n\
ull\x0a        }\x0a  \
  }\x0a\x0a    propert\
y string valueSt\
ring: obj ? obj.\
valueString : ''\
\x0a    property va\
r value: null\x0a\x0a \
   property bool\
 refreshed: fals\
e\x0a\x0a    Timer {\x0a \
       id: updat\
edTimer\x0a        \
interval: 1100\x0a \
       onTrigger\
ed: comp.refresh\
ed = false\x0a    }\
\x0a\x0a    onValueStr\
ingChanged: {\x0a  \
      if(obj)\x0a  \
          value \
= obj.valueSafe\x0a\
\x0a        comp.re\
freshed = true\x0a \
       updatedTi\
mer.restart()\x0a  \
  }\x0a\x0a    functio\
n set(x) {\x0a     \
   if(obj)\x0a     \
       obj.value\
String = x\x0a    }\
\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x09\
\x09\xab\xcdT\
\x00L\
\x00i\x00b\x00s\x00t\x00o\x00r\x00e\x00d\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0a\
\x07n\x093\
\x00C\
\x00o\x00m\x00p\x00o\x00n\x00e\x00n\x00t\x00s\
\x00\x0f\
\x0d\x0f\x0a\xbc\
\x00M\
\x00e\x00a\x00s\x00u\x00r\x00e\x00m\x00e\x00n\x00t\x00.\x00q\x00m\x00l\
\x00\x09\
\x07\xc7\xf8\x9c\
\x00I\
\x00n\x00p\x00u\x00t\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x84+\x02\
\x00q\
\x00m\x00l\x00d\x00i\x00r\
\x00\x0f\
\x06\xb2\x90\xfc\
\x00S\
\x00t\x00o\x00r\x00e\x00O\x00b\x00j\x00e\x00c\x00t\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8a\xcbQ,\xf9\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00.\x00\x02\x00\x00\x00\x04\x00\x00\x00\x04\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x96\x00\x00\x00\x00\x00\x01\x00\x00\x11\xaf\
\x00\x00\x01\x8a\xcbQ,\xf9\
\x00\x00\x00\x84\x00\x00\x00\x00\x00\x01\x00\x00\x10\xe2\
\x00\x00\x01\x8a\xcbQ,\xf9\
\x00\x00\x00l\x00\x00\x00\x00\x00\x01\x00\x00\x0bW\
\x00\x00\x01\x8a\xcbQ,\xf9\
\x00\x00\x00H\x00\x00\x00\x00\x00\x01\x00\x00\x05\xe9\
\x00\x00\x01\x8a\xcbQ,\xf9\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
