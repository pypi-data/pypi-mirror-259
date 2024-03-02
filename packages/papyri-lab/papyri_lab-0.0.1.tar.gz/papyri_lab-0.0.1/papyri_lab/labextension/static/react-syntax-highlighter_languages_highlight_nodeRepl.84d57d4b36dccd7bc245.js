(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["react-syntax-highlighter_languages_highlight_nodeRepl"],{

/***/ "./node_modules/highlight.js/lib/languages/node-repl.js":
/*!**************************************************************!*\
  !*** ./node_modules/highlight.js/lib/languages/node-repl.js ***!
  \**************************************************************/
/***/ ((module) => {

/*
Language: Node REPL
Requires: javascript.js
Author: Marat Nagayev <nagaevmt@yandex.ru>
Category: scripting
*/

/** @type LanguageFn */
function nodeRepl(hljs) {
  return {
    name: 'Node REPL',
    contains: [
      {
        className: 'meta',
        starts: {
          // a space separates the REPL prefix from the actual code
          // this is purely for cleaner HTML output
          end: / |$/,
          starts: {
            end: '$',
            subLanguage: 'javascript'
          }
        },
        variants: [
          {
            begin: /^>(?=[ ]|$)/
          },
          {
            begin: /^\.\.\.(?=[ ]|$)/
          }
        ]
      }
    ]
  };
}

module.exports = nodeRepl;


/***/ })

}]);
//# sourceMappingURL=react-syntax-highlighter_languages_highlight_nodeRepl.84d57d4b36dccd7bc245.js.map