(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["react-syntax-highlighter_languages_highlight_clean"],{

/***/ "./node_modules/highlight.js/lib/languages/clean.js":
/*!**********************************************************!*\
  !*** ./node_modules/highlight.js/lib/languages/clean.js ***!
  \**********************************************************/
/***/ ((module) => {

/*
Language: Clean
Author: Camil Staps <info@camilstaps.nl>
Category: functional
Website: http://clean.cs.ru.nl
*/

/** @type LanguageFn */
function clean(hljs) {
  return {
    name: 'Clean',
    aliases: [
      'icl',
      'dcl'
    ],
    keywords: {
      keyword:
        'if let in with where case of class instance otherwise ' +
        'implementation definition system module from import qualified as ' +
        'special code inline foreign export ccall stdcall generic derive ' +
        'infix infixl infixr',
      built_in:
        'Int Real Char Bool',
      literal:
        'True False'
    },
    contains: [
      hljs.C_LINE_COMMENT_MODE,
      hljs.C_BLOCK_COMMENT_MODE,
      hljs.APOS_STRING_MODE,
      hljs.QUOTE_STRING_MODE,
      hljs.C_NUMBER_MODE,
      { // relevance booster
        begin: '->|<-[|:]?|#!?|>>=|\\{\\||\\|\\}|:==|=:|<>'
      }
    ]
  };
}

module.exports = clean;


/***/ })

}]);
//# sourceMappingURL=react-syntax-highlighter_languages_highlight_clean.3d39b6f608f9901feda3.js.map