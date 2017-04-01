# -*- coding: utf-8 -*-
accepted_langs_normal =["ALGOL", "Atlas Autocode", "ALGOL 58 ", "IAL", "International Algorithmic Language", "MAD", "GOM", "Michigan Algorithm Decoder", "Good Old MAD", "ALGOL 60", "MAD/I", "Simula", "ALGOL 68", "ALGOL W", "Pascal", "Ada", "SPARK", "PL/SQL", "Turbo Pascal", "Object Pascal", "Free Pascal", "FPC", "Kylix", "Delphi", "Euclid", "Concurrent Euclid", "Turing", "Turing Plus", "Object Oriented Turing", "Modula-2", "Modula-3", "Oberon ", "Oberon-1", "Oberon-2", "Component Pascal", "Active Oberon", "Zonnon", "Oberon-07", "SUE", "Plus", "CPL", "BCPL", "B", "APL", "A+", "J", "K", "NESL", "BASIC", "AmigaBASIC", "AMOS BASIC", "BASIC Stamp", "BASIC09", "Basic4GL", "BBC Basic", "Blitz BASIC", "Blitz3D", "BlitzMax", "BlitzPlus", "Business Basic", "Caché Basic", "Chinese BASIC", "COMAL", "Commodore BASIC", "DarkBASIC", "DarkBASIC Professional", "Euphoria", "GW-BASIC", "QuickBASIC", "QBasic", "FreeBASIC", "Liberty BASIC", "Run BASIC", "Visual Basic", "VBScript", "Visual Basic for Applications", "VBA", "LotusScript", "Visual Basic .NET", "Small Basic", "OpenOffice Basic", "Gambas", "WinWrap Basic", "WordBasic", "QB64", "GLBasic", "PureBasic", "Turbo Basic", "PowerBASIC", "REALbasic", "Xojo", "thinBasic", "TI-BASIC", "True BASIC", "YaBasic", "XBasic", "MS-DOS Batch files", "Winbatch", "CLIST", "IBM Job Control Language", "IBM JCL", "C", "Alef", "C++", "C#", "Cobra", "Java", "Rust", "C--", "Cyclone", "Rust", "D", "ColdFusion", "Go", "Harbour", "Limbo", "LPC", "Pike", "PCASTL", "Perl", "Windows PowerShell", "S2", "PHP", "Julia", "Swift", "PDL", "Python", "Nim", "QuakeC", "COBOL", "ABAP", "DIBOL", "WATBOL", "COMIT", "SNOBOL", "Icon", "Unicon", "Lua", "ed", "sed", "AWK", "Eiffel", "Cobra", "Sather", "Ubercode", "Forth", "InterPress", "PostScript", "Joy", "Factor", "Rebol", "RPL", "Fortran", "Fortran II", "Fortran IV", "WATFOR", "WATFIV", "Fortran 66", "FORMAC", "Ratfor", "Fortran 77", "WATFOR-77", "Ratfiv", "Fortran 90", "Fortran 95", "F", "Fortran 2003", "FP", "Function Programming", "FL", "Function Level", "FPr", "HyperTalk", "ActionScript", "AppleScript", "SenseTalk", "SuperTalk", "Transcript", "Ateji PX", "Ceylon", "Fantom", "Apache Groovy", "OptimJ", "Processing", "Scala", "Join Java", "J#", "Kotlin", "X10", "Asm.js", "CoffeeScript", "ECMAScript", "Haxe", "JavaScript OSA", "JScript", "TypeScript", "JOSS", "CAL", "TELCOMP", "FOCAL", "MUMPS", "Caché ObjectScript", "Lisp", "Arc", "AutoLISP", "Clojure", "Common Lisp", "Emacs Lisp", "LFE", "Logo", "Turtle", "Nu", "PicoLisp", "REBOL", "Red", "S", "R", "Scheme", "GNU Guile", "Racket", "Hop", "Pico", "T", "ML", "Standard ML", "SML", "Caml", "OCaml", "F#", "PL/I", "PL/M", "PL/C", "REXX", "SP/k", "XPL", "Prolog", "CLP(R)", "CLP(FD)", "Mercury", "Erlang", "Logtalk", "SASL", "Kent Recursive Calculator", "Miranda", "Haskell", "Agda", "Idris", "SETL", "ABC", "Boo", "Sh", "bash", "tcsh", "zsh", "ksh", "Smalltalk", "Cobra", "Ruby", "Self", "NewtonScript", "Io", "BETA", "Assembly", "BLISS", "CORAL", "Curl", "GPSS", "LabVIEW", "NXT-G", "occam", "POP-2, POP-11", "REFAL", "RPG", "Report Program Generator", "Seed7", "TACL", "Tandem Advanced Command Language", "TUTOR", "Tcl", "Expect", "Tea"]
accepted_langs_lower = ["algol", "atlas autocode", "algol 58 ", "ial", "international algorithmic language", "mad", "gom", "michigan algorithm decoder", "good old mad", "algol 60", "mad/i", "simula", "algol 68", "algol w", "pascal", "ada", "spark", "pl/sql", "turbo pascal", "object pascal", "free pascal", "fpc", "kylix", "delphi", "euclid", "concurrent euclid", "turing", "turing plus", "object oriented turing", "modula-2", "modula-3", "oberon ", "oberon-1", "oberon-2", "component pascal", "active oberon", "zonnon", "oberon-07", "sue", "plus", "cpl", "bcpl", "b", "apl", "a+", "j", "k", "nesl", "basic", "amigabasic", "amos basic", "basic stamp", "basic09", "basic4gl", "bbc basic", "blitz basic", "blitz3d", "blitzmax", "blitzplus", "business basic", "caché basic", "chinese basic", "comal", "commodore basic", "darkbasic", "darkbasic professional", "euphoria", "gw-basic", "quickbasic", "qbasic", "freebasic", "liberty basic", "run basic", "visual basic", "vbscript", "visual basic for applications", "vba", "lotusscript", "visual basic .net", "small basic", "openoffice basic", "gambas", "winwrap basic", "wordbasic", "qb64", "glbasic", "purebasic", "turbo basic", "powerbasic", "realbasic", "xojo", "thinbasic", "ti-basic", "true basic", "yabasic", "xbasic", "ms-dos batch files", "winbatch", "clist", "ibm job control language", "ibm jcl", "c", "alef", "c++", "c#", "cobra", "java", "rust", "c--", "cyclone", "rust", "d", "coldfusion", "go", "harbour", "limbo", "lpc", "pike", "pcastl", "perl", "windows powershell", "s2", "php", "julia", "swift", "pdl", "python", "nim", "quakec", "cobol", "abap", "dibol", "watbol", "comit", "snobol", "icon", "unicon", "lua", "ed", "sed", "awk", "eiffel", "cobra", "sather", "ubercode", "forth", "interpress", "postscript", "joy", "factor", "rebol", "rpl", "fortran", "fortran ii", "fortran iv", "watfor", "watfiv", "fortran 66", "formac", "ratfor", "fortran 77", "watfor-77", "ratfiv", "fortran 90", "fortran 95", "f", "fortran 2003", "fp", "function programming", "fl", "function level", "fpr", "hypertalk", "actionscript", "applescript", "sensetalk", "supertalk", "transcript", "ateji px", "ceylon", "fantom", "apache groovy", "optimj", "processing", "scala", "join java", "j#", "kotlin", "x10", "asm.js", "coffeescript", "ecmascript", "haxe", "javascript osa", "jscript", "typescript", "joss", "cal", "telcomp", "focal", "mumps", "caché objectscript", "lisp", "arc", "autolisp", "clojure", "common lisp", "emacs lisp", "lfe", "logo", "turtle", "nu", "picolisp", "rebol", "red", "s", "r", "scheme", "gnu guile", "racket", "hop", "pico", "t", "ml", "standard ml", "sml", "caml", "ocaml", "f#", "pl/i", "pl/m", "pl/c", "rexx", "sp/k", "xpl", "prolog", "clp(r)", "clp(fd)", "mercury", "erlang", "logtalk", "sasl", "kent recursive calculator", "miranda", "haskell", "agda", "idris", "setl", "abc", "boo", "sh", "bash", "tcsh", "zsh", "ksh", "smalltalk", "cobra", "ruby", "self", "newtonscript", "io", "beta", "assembly", "bliss", "coral", "curl", "gpss", "labview", "nxt-g", "occam", "pop-2, pop-11", "refal", "rpg", "report program generator", "seed7", "tacl", "tandem advanced command language", "tutor", "tcl", "expect", "tea"]