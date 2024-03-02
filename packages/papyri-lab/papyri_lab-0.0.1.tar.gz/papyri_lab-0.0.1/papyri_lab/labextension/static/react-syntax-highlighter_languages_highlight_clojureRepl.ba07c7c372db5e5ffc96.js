(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["react-syntax-highlighter_languages_highlight_clojureRepl"],{

/***/ "./node_modules/highlight.js/lib/languages/clojure-repl.js":
/*!*****************************************************************!*\
  !*** ./node_modules/highlight.js/lib/languages/clojure-repl.js ***!
  \*****************************************************************/
/***/ ((module) => {

/*
Language: Clojure REPL
Description: Clojure REPL sessions
Author: Ivan Sagalaev <maniac@softwaremaniacs.org>
Requires: clojure.js
Website: https://clojure.org
Category: lisp
*/

/** @type LanguageFn */
function clojureRepl(hljs) {
  return {
    name: 'Clojure REPL',
    contains: [
      {
        className: 'meta',
        begin: /^([\w.-]+|\s*#_)?=>/,
        starts: {
          end: /$/,
          subLanguage: 'clojure'
        }
      }
    ]
  };
}

module.exports = clojureRepl;


/***/ })

}]);
//# sourceMappingURL=react-syntax-highlighter_languages_highlight_clojureRepl.ba07c7c372db5e5ffc96.js.map