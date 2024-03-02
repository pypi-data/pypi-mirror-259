(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["react-syntax-highlighter_languages_highlight_brainfuck"],{

/***/ "./node_modules/highlight.js/lib/languages/brainfuck.js":
/*!**************************************************************!*\
  !*** ./node_modules/highlight.js/lib/languages/brainfuck.js ***!
  \**************************************************************/
/***/ ((module) => {

/*
Language: Brainfuck
Author: Evgeny Stepanischev <imbolk@gmail.com>
Website: https://esolangs.org/wiki/Brainfuck
*/

/** @type LanguageFn */
function brainfuck(hljs) {
  const LITERAL = {
    className: 'literal',
    begin: /[+-]/,
    relevance: 0
  };
  return {
    name: 'Brainfuck',
    aliases: ['bf'],
    contains: [
      hljs.COMMENT(
        '[^\\[\\]\\.,\\+\\-<> \r\n]',
        '[\\[\\]\\.,\\+\\-<> \r\n]',
        {
          returnEnd: true,
          relevance: 0
        }
      ),
      {
        className: 'title',
        begin: '[\\[\\]]',
        relevance: 0
      },
      {
        className: 'string',
        begin: '[\\.,]',
        relevance: 0
      },
      {
        // this mode works as the only relevance counter
        begin: /(?:\+\+|--)/,
        contains: [LITERAL]
      },
      LITERAL
    ]
  };
}

module.exports = brainfuck;


/***/ })

}]);
//# sourceMappingURL=react-syntax-highlighter_languages_highlight_brainfuck.c56efeb76b0531e196f3.js.map