(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["react-syntax-highlighter_languages_highlight_diff"],{

/***/ "./node_modules/highlight.js/lib/languages/diff.js":
/*!*********************************************************!*\
  !*** ./node_modules/highlight.js/lib/languages/diff.js ***!
  \*********************************************************/
/***/ ((module) => {

/*
Language: Diff
Description: Unified and context diff
Author: Vasily Polovnyov <vast@whiteants.net>
Website: https://www.gnu.org/software/diffutils/
Category: common
*/

/** @type LanguageFn */
function diff(hljs) {
  return {
    name: 'Diff',
    aliases: ['patch'],
    contains: [
      {
        className: 'meta',
        relevance: 10,
        variants: [
          {
            begin: /^@@ +-\d+,\d+ +\+\d+,\d+ +@@/
          },
          {
            begin: /^\*\*\* +\d+,\d+ +\*\*\*\*$/
          },
          {
            begin: /^--- +\d+,\d+ +----$/
          }
        ]
      },
      {
        className: 'comment',
        variants: [
          {
            begin: /Index: /,
            end: /$/
          },
          {
            begin: /^index/,
            end: /$/
          },
          {
            begin: /={3,}/,
            end: /$/
          },
          {
            begin: /^-{3}/,
            end: /$/
          },
          {
            begin: /^\*{3} /,
            end: /$/
          },
          {
            begin: /^\+{3}/,
            end: /$/
          },
          {
            begin: /^\*{15}$/
          },
          {
            begin: /^diff --git/,
            end: /$/
          }
        ]
      },
      {
        className: 'addition',
        begin: /^\+/,
        end: /$/
      },
      {
        className: 'deletion',
        begin: /^-/,
        end: /$/
      },
      {
        className: 'addition',
        begin: /^!/,
        end: /$/
      }
    ]
  };
}

module.exports = diff;


/***/ })

}]);
//# sourceMappingURL=react-syntax-highlighter_languages_highlight_diff.c5831f348a3bbcdee105.js.map