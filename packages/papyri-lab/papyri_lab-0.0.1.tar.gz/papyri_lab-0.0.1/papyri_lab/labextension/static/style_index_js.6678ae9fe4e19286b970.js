"use strict";
(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["style_index_js"],{

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/***/ ((module) => {



/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
module.exports = function (cssWithMappingToString) {
  var list = [];

  // return the list of modules as css string
  list.toString = function toString() {
    return this.map(function (item) {
      var content = "";
      var needLayer = typeof item[5] !== "undefined";
      if (item[4]) {
        content += "@supports (".concat(item[4], ") {");
      }
      if (item[2]) {
        content += "@media ".concat(item[2], " {");
      }
      if (needLayer) {
        content += "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {");
      }
      content += cssWithMappingToString(item);
      if (needLayer) {
        content += "}";
      }
      if (item[2]) {
        content += "}";
      }
      if (item[4]) {
        content += "}";
      }
      return content;
    }).join("");
  };

  // import a list of modules into the list
  list.i = function i(modules, media, dedupe, supports, layer) {
    if (typeof modules === "string") {
      modules = [[null, modules, undefined]];
    }
    var alreadyImportedModules = {};
    if (dedupe) {
      for (var k = 0; k < this.length; k++) {
        var id = this[k][0];
        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }
    for (var _k = 0; _k < modules.length; _k++) {
      var item = [].concat(modules[_k]);
      if (dedupe && alreadyImportedModules[item[0]]) {
        continue;
      }
      if (typeof layer !== "undefined") {
        if (typeof item[5] === "undefined") {
          item[5] = layer;
        } else {
          item[1] = "@layer".concat(item[5].length > 0 ? " ".concat(item[5]) : "", " {").concat(item[1], "}");
          item[5] = layer;
        }
      }
      if (media) {
        if (!item[2]) {
          item[2] = media;
        } else {
          item[1] = "@media ".concat(item[2], " {").concat(item[1], "}");
          item[2] = media;
        }
      }
      if (supports) {
        if (!item[4]) {
          item[4] = "".concat(supports);
        } else {
          item[1] = "@supports (".concat(item[4], ") {").concat(item[1], "}");
          item[4] = supports;
        }
      }
      list.push(item);
    }
  };
  return list;
};

/***/ }),

/***/ "./node_modules/css-loader/dist/runtime/sourceMaps.js":
/*!************************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/sourceMaps.js ***!
  \************************************************************/
/***/ ((module) => {



module.exports = function (item) {
  var content = item[1];
  var cssMapping = item[3];
  if (!cssMapping) {
    return content;
  }
  if (typeof btoa === "function") {
    var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(cssMapping))));
    var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
    var sourceMapping = "/*# ".concat(data, " */");
    return [content].concat([sourceMapping]).join("\n");
  }
  return [content].join("\n");
};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js":
/*!****************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js ***!
  \****************************************************************************/
/***/ ((module) => {



var stylesInDOM = [];
function getIndexByIdentifier(identifier) {
  var result = -1;
  for (var i = 0; i < stylesInDOM.length; i++) {
    if (stylesInDOM[i].identifier === identifier) {
      result = i;
      break;
    }
  }
  return result;
}
function modulesToDom(list, options) {
  var idCountMap = {};
  var identifiers = [];
  for (var i = 0; i < list.length; i++) {
    var item = list[i];
    var id = options.base ? item[0] + options.base : item[0];
    var count = idCountMap[id] || 0;
    var identifier = "".concat(id, " ").concat(count);
    idCountMap[id] = count + 1;
    var indexByIdentifier = getIndexByIdentifier(identifier);
    var obj = {
      css: item[1],
      media: item[2],
      sourceMap: item[3],
      supports: item[4],
      layer: item[5]
    };
    if (indexByIdentifier !== -1) {
      stylesInDOM[indexByIdentifier].references++;
      stylesInDOM[indexByIdentifier].updater(obj);
    } else {
      var updater = addElementStyle(obj, options);
      options.byIndex = i;
      stylesInDOM.splice(i, 0, {
        identifier: identifier,
        updater: updater,
        references: 1
      });
    }
    identifiers.push(identifier);
  }
  return identifiers;
}
function addElementStyle(obj, options) {
  var api = options.domAPI(options);
  api.update(obj);
  var updater = function updater(newObj) {
    if (newObj) {
      if (newObj.css === obj.css && newObj.media === obj.media && newObj.sourceMap === obj.sourceMap && newObj.supports === obj.supports && newObj.layer === obj.layer) {
        return;
      }
      api.update(obj = newObj);
    } else {
      api.remove();
    }
  };
  return updater;
}
module.exports = function (list, options) {
  options = options || {};
  list = list || [];
  var lastIdentifiers = modulesToDom(list, options);
  return function update(newList) {
    newList = newList || [];
    for (var i = 0; i < lastIdentifiers.length; i++) {
      var identifier = lastIdentifiers[i];
      var index = getIndexByIdentifier(identifier);
      stylesInDOM[index].references--;
    }
    var newLastIdentifiers = modulesToDom(newList, options);
    for (var _i = 0; _i < lastIdentifiers.length; _i++) {
      var _identifier = lastIdentifiers[_i];
      var _index = getIndexByIdentifier(_identifier);
      if (stylesInDOM[_index].references === 0) {
        stylesInDOM[_index].updater();
        stylesInDOM.splice(_index, 1);
      }
    }
    lastIdentifiers = newLastIdentifiers;
  };
};

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/insertBySelector.js":
/*!********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/insertBySelector.js ***!
  \********************************************************************/
/***/ ((module) => {



var memo = {};

/* istanbul ignore next  */
function getTarget(target) {
  if (typeof memo[target] === "undefined") {
    var styleTarget = document.querySelector(target);

    // Special case to return head of iframe instead of iframe itself
    if (window.HTMLIFrameElement && styleTarget instanceof window.HTMLIFrameElement) {
      try {
        // This will throw an exception if access to iframe is blocked
        // due to cross-origin restrictions
        styleTarget = styleTarget.contentDocument.head;
      } catch (e) {
        // istanbul ignore next
        styleTarget = null;
      }
    }
    memo[target] = styleTarget;
  }
  return memo[target];
}

/* istanbul ignore next  */
function insertBySelector(insert, style) {
  var target = getTarget(insert);
  if (!target) {
    throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
  }
  target.appendChild(style);
}
module.exports = insertBySelector;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/insertStyleElement.js":
/*!**********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/insertStyleElement.js ***!
  \**********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function insertStyleElement(options) {
  var element = document.createElement("style");
  options.setAttributes(element, options.attributes);
  options.insert(element, options.options);
  return element;
}
module.exports = insertStyleElement;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js":
/*!**********************************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js ***!
  \**********************************************************************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {



/* istanbul ignore next  */
function setAttributesWithoutAttributes(styleElement) {
  var nonce =  true ? __webpack_require__.nc : 0;
  if (nonce) {
    styleElement.setAttribute("nonce", nonce);
  }
}
module.exports = setAttributesWithoutAttributes;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/styleDomAPI.js":
/*!***************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/styleDomAPI.js ***!
  \***************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function apply(styleElement, options, obj) {
  var css = "";
  if (obj.supports) {
    css += "@supports (".concat(obj.supports, ") {");
  }
  if (obj.media) {
    css += "@media ".concat(obj.media, " {");
  }
  var needLayer = typeof obj.layer !== "undefined";
  if (needLayer) {
    css += "@layer".concat(obj.layer.length > 0 ? " ".concat(obj.layer) : "", " {");
  }
  css += obj.css;
  if (needLayer) {
    css += "}";
  }
  if (obj.media) {
    css += "}";
  }
  if (obj.supports) {
    css += "}";
  }
  var sourceMap = obj.sourceMap;
  if (sourceMap && typeof btoa !== "undefined") {
    css += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap)))), " */");
  }

  // For old IE
  /* istanbul ignore if  */
  options.styleTagTransform(css, styleElement, options.options);
}
function removeStyleElement(styleElement) {
  // istanbul ignore if
  if (styleElement.parentNode === null) {
    return false;
  }
  styleElement.parentNode.removeChild(styleElement);
}

/* istanbul ignore next  */
function domAPI(options) {
  if (typeof document === "undefined") {
    return {
      update: function update() {},
      remove: function remove() {}
    };
  }
  var styleElement = options.insertStyleElement(options);
  return {
    update: function update(obj) {
      apply(styleElement, options, obj);
    },
    remove: function remove() {
      removeStyleElement(styleElement);
    }
  };
}
module.exports = domAPI;

/***/ }),

/***/ "./node_modules/style-loader/dist/runtime/styleTagTransform.js":
/*!*********************************************************************!*\
  !*** ./node_modules/style-loader/dist/runtime/styleTagTransform.js ***!
  \*********************************************************************/
/***/ ((module) => {



/* istanbul ignore next  */
function styleTagTransform(css, styleElement) {
  if (styleElement.styleSheet) {
    styleElement.styleSheet.cssText = css;
  } else {
    while (styleElement.firstChild) {
      styleElement.removeChild(styleElement.firstChild);
    }
    styleElement.appendChild(document.createTextNode(css));
  }
}
module.exports = styleTagTransform;

/***/ }),

/***/ "./style/index.js":
/*!************************!*\
  !*** ./style/index.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _base_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./base.css */ "./style/base.css");



/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./style/app.css":
/*!*************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/app.css ***!
  \*************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/sourceMaps.js */ "./node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
// Imports


var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
// Module
___CSS_LOADER_EXPORT___.push([module.id, `.container{width:100%}@media (min-width:640px){.container{max-width:640px}}@media (min-width:768px){.container{max-width:768px}}@media (min-width:1024px){.container{max-width:1024px}}@media (min-width:1280px){.container{max-width:1280px}}@media (min-width:1536px){.container{max-width:1536px}}.prose{color:var(--tw-prose-body);max-width:65ch}.prose :where(p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:1em;color:var(--jp-content-font-color1);font-family:var(--jp-content-font-family);font-size:var(--jp-content-font-size1);line-height:var(--jp-content-line-height)}.prose :where([class~=lead]):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-lead);font-size:1.25em;line-height:1.6;margin-top:1.2em;margin-bottom:1.2em}.prose :where(a):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--jp-content-link-color,#1976d2);text-decoration:none;font-weight:400}.prose :where(a):not(:where([class~=not-prose],[class~=not-prose] *)):hover{color:var(--jp-content-link-color,#1976d2);text-decoration:underline;font-weight:400}.prose :where(strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-bold);font-weight:600}.prose :where(a strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(blockquote strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(thead th strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(ol):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:decimal;margin-top:1.25em;margin-bottom:1.25em;padding-left:1.625em}.prose :where(ol[type=A]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-alpha}.prose :where(ol[type=a]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-alpha}.prose :where(ol[type=A s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-alpha}.prose :where(ol[type=a s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-alpha}.prose :where(ol[type=I]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-roman}.prose :where(ol[type=i]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-roman}.prose :where(ol[type=I s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-roman}.prose :where(ol[type=i s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-roman}.prose :where(ol[type="1"]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:decimal}.prose :where(ul):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:disc;margin-top:1.25em;margin-bottom:1.25em;padding-left:1.625em}.prose :where(ol>li):not(:where([class~=not-prose],[class~=not-prose] *))::marker{font-weight:400;color:var(--tw-prose-counters)}.prose :where(ul>li):not(:where([class~=not-prose],[class~=not-prose] *))::marker{color:var(--tw-prose-bullets)}.prose :where(dt):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;margin-top:1.25em}.prose :where(hr):not(:where([class~=not-prose],[class~=not-prose] *)){border-color:var(--tw-prose-hr);border-top-width:1px;margin-top:3em;margin-bottom:3em}.prose :where(blockquote):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:500;font-style:italic;color:var(--tw-prose-quotes);border-left-width:.25rem;border-left-color:var(--tw-prose-quote-borders);quotes:"\\201C""\\201D""\\2018""\\2019";margin-top:1.6em;margin-bottom:1.6em;padding-left:1em}.prose :where(blockquote p:first-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):before{content:none}.prose :where(blockquote p:last-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:close-quote}.prose :where(h1):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:800;font-size:var(--jp-content-font-size5);margin-top:0;margin-bottom:.8888889em;line-height:1.1111111}.prose :where(h1 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:900;color:inherit}.prose :where(h2):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:700;font-size:var(--jp-content-font-size4);margin-top:2em;margin-bottom:1em;line-height:1.3333333}.prose :where(h2 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:800;color:inherit}.prose :where(h3):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;font-size:var(--jp-content-font-size3);margin-top:1.6em;margin-bottom:.6em;line-height:1.6}.prose :where(h3 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:700;color:inherit}.prose :where(h4):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;margin-top:1.5em;margin-bottom:.5em;line-height:1.5;font-size:var(--jp-content-font-size2)}.prose :where(h4 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:700;color:inherit}.prose :where(img):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(picture):not(:where([class~=not-prose],[class~=not-prose] *)){display:block;margin-top:2em;margin-bottom:2em}.prose :where(kbd):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:500;font-family:inherit;color:var(--tw-prose-kbd);box-shadow:0 0 0 1px rgb(var(--tw-prose-kbd-shadows)/10%),0 3px 0 rgb(var(--tw-prose-kbd-shadows)/10%);font-size:.875em;border-radius:.3125rem;padding:.1875em .375em}.prose :where(code):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--jp-content-font-color1);font-weight:inherit;font-size:inherit;font-family:var(--jp-code-font-family);line-height:var(--jp-code-line-height);padding:1px 5px;white-space:pre-wrap;background-color:var(--jp-layout-color2)}.prose :where(a code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(h1 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(h2 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit;font-size:.875em}.prose :where(h3 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit;font-size:.9em}.prose :where(h4 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(blockquote code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(thead th code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(pre):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-pre-code);background-color:var(--tw-prose-pre-bg);overflow-x:auto;font-weight:400;font-size:.875em;line-height:1.7142857;margin-top:1.7142857em;margin-bottom:1.7142857em;border-radius:.375rem;padding:.8571429em 1.1428571em}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)){background-color:initial;border-width:0;border-radius:0;padding:0;font-weight:inherit;color:inherit;font-size:inherit;font-family:inherit;line-height:inherit}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)):before{content:none}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:none}.prose :where(table):not(:where([class~=not-prose],[class~=not-prose] *)){width:100%;table-layout:auto;text-align:left;margin-top:2em;margin-bottom:2em;font-size:.875em;line-height:1.7142857}.prose :where(thead):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:1px;border-bottom-color:var(--tw-prose-th-borders)}.prose :where(thead th):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;vertical-align:bottom;padding-right:.5714286em;padding-bottom:.5714286em;padding-left:.5714286em}.prose :where(tbody tr):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:1px;border-bottom-color:var(--tw-prose-td-borders)}.prose :where(tbody tr:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:0}.prose :where(tbody td):not(:where([class~=not-prose],[class~=not-prose] *)){vertical-align:initial}.prose :where(tfoot):not(:where([class~=not-prose],[class~=not-prose] *)){border-top-width:1px;border-top-color:var(--tw-prose-th-borders)}.prose :where(tfoot td):not(:where([class~=not-prose],[class~=not-prose] *)){vertical-align:top}.prose :where(figure>*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:0}.prose :where(figcaption):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-captions);font-size:.875em;line-height:1.4285714;margin-top:.8571429em}.prose{--tw-prose-body:#374151;--tw-prose-headings:#111827;--tw-prose-lead:#4b5563;--tw-prose-links:#111827;--tw-prose-bold:#111827;--tw-prose-counters:#6b7280;--tw-prose-bullets:#d1d5db;--tw-prose-hr:#e5e7eb;--tw-prose-quotes:#111827;--tw-prose-quote-borders:#e5e7eb;--tw-prose-captions:#6b7280;--tw-prose-kbd:#111827;--tw-prose-kbd-shadows:17 24 39;--tw-prose-code:#111827;--tw-prose-pre-code:#e5e7eb;--tw-prose-pre-bg:#1f2937;--tw-prose-th-borders:#d1d5db;--tw-prose-td-borders:#e5e7eb;--tw-prose-invert-body:#d1d5db;--tw-prose-invert-headings:#fff;--tw-prose-invert-lead:#9ca3af;--tw-prose-invert-links:#fff;--tw-prose-invert-bold:#fff;--tw-prose-invert-counters:#9ca3af;--tw-prose-invert-bullets:#4b5563;--tw-prose-invert-hr:#374151;--tw-prose-invert-quotes:#f3f4f6;--tw-prose-invert-quote-borders:#374151;--tw-prose-invert-captions:#9ca3af;--tw-prose-invert-kbd:#fff;--tw-prose-invert-kbd-shadows:255 255 255;--tw-prose-invert-code:#fff;--tw-prose-invert-pre-code:#d1d5db;--tw-prose-invert-pre-bg:#00000080;--tw-prose-invert-th-borders:#4b5563;--tw-prose-invert-td-borders:#374151;font-size:1rem;line-height:1.75}.prose :where(picture>img):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:0}.prose :where(video):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(li):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.25rem;margin-bottom:.25rem}.prose :where(ol>li):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:.375em}.prose :where(ul>li):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:.375em}.prose :where(.prose>ul>li p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.75em;margin-bottom:.75em}.prose :where(.prose>ul>li>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em}.prose :where(.prose>ul>li>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:1.25em}.prose :where(.prose>ol>li>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em}.prose :where(.prose>ol>li>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:1.25em}.prose :where(ul ul,ul ol,ol ul,ol ol):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.75em;margin-bottom:.75em}.prose :where(dl):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em;margin-bottom:1.25em}.prose :where(dd):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.5em;padding-left:1.625em}.prose :where(hr+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h2+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h3+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h4+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(thead th:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:0}.prose :where(thead th:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-right:0}.prose :where(tbody td,tfoot td):not(:where([class~=not-prose],[class~=not-prose] *)){padding:.5714286em}.prose :where(tbody td:first-child,tfoot td:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:0}.prose :where(tbody td:last-child,tfoot td:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-right:0}.prose :where(figure):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(.prose>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(.prose>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:0}.prose :where(h1,h2,h3,h4,h5,h6):not(:where([class~=not-prose],[class~=not-prose] *)){line-height:var(--jp-content-heading-line-height,1);font-weight:var(--jp-content-heading-font-weight,500);font-style:normal;margin-top:var(--jp-content-heading-margin-top,1.2em);margin-bottom:var(--jp-content-heading-margin-bottom,.8em);color:var(--jp-content-font-color1)}.prose :where(h1:first-child,h2:first-child,h3:first-child,h4:first-child,h5:first-child,h6:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:calc(var(--jp-content-heading-margin-top)*.5)}.prose :where(h1:last-child,h2:last-child,h3:last-child,h4:last-child,h5:last-child,h6:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:calc(var(--jp-content-heading-margin-bottom)*.5)}.prose :where(h5):not(:where([class~=not-prose],[class~=not-prose] *)){font-size:var(--jp-content-font-size1)}.prose :where(h6):not(:where([class~=not-prose],[class~=not-prose] *)){font-size:var(--jp-content-font-size0)}.prose :where(blockquote p:first-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:none}.prose :where(li>p,dd>p,header>p,footer>p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.25rem;margin-bottom:.25rem}.static{position:static}.absolute{position:absolute}.relative{position:relative}.right-1{right:.25rem}.top-1{top:.25rem}.top-\\[32px\\]{top:32px}.float-right{float:right}.m-0{margin:0}.my-2{margin-top:.5rem;margin-bottom:.5rem}.my-5{margin-top:1.25rem;margin-bottom:1.25rem}.mb-4{margin-bottom:1rem}.ml-1{margin-left:.25rem}.ml-2{margin-left:.5rem}.ml-3{margin-left:.75rem}.ml-4{margin-left:1rem}.mr-1{margin-right:.25rem}.mr-2{margin-right:.5rem}.mr-3{margin-right:.75rem}.mt-2{margin-top:.5rem}.mt-3{margin-top:.75rem}.block{display:block}.inline-block{display:inline-block}.inline{display:inline}.flex{display:flex}.inline-flex{display:inline-flex}.table{display:table}.grid{display:grid}.hidden{display:none}.h-4{height:1rem}.h-\\[10px\\]{height:10px}.h-\\[150px\\]{height:150px}.h-full{height:100%}.max-h-\\[300px\\]{max-height:300px}.max-h-\\[4rem\\]{max-height:4rem}.min-h-\\[2em\\]{min-height:2em}.w-4{width:1rem}.w-\\[10px\\]{width:10px}.w-\\[300px\\]{width:300px}.w-\\[400px\\]{width:400px}.w-\\[500px\\]{width:500px}.w-full{width:100%}.min-w-0{min-width:0}.max-w-\\[80vw\\]{max-width:80vw}.flex-1{flex:1 1 0%}.flex-none{flex:none}.flex-grow,.grow{flex-grow:1}.-translate-y-\\[1px\\],.-translate-y-px{--tw-translate-y:-1px}.-translate-y-\\[1px\\],.-translate-y-px,.translate-y-2{transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.translate-y-2{--tw-translate-y:0.5rem}.transform{transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}@keyframes pulse{50%{opacity:.5}}.animate-pulse{animation:pulse 2s cubic-bezier(.4,0,.6,1) infinite}.cursor-help{cursor:help}.cursor-pointer{cursor:pointer}.select-none{-webkit-user-select:none;-moz-user-select:none;user-select:none}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}.flex-row{flex-direction:row}.flex-col{flex-direction:column}.flex-wrap{flex-wrap:wrap}.items-center{align-items:center}.gap-4{gap:1rem}.self-center{align-self:center}.overflow-auto{overflow:auto}.overflow-hidden{overflow:hidden}.overflow-x-auto{overflow-x:auto}.overflow-y-hidden{overflow-y:hidden}.break-words{overflow-wrap:break-word}.rounded{border-radius:.25rem}.rounded-full{border-radius:9999px}.rounded-md{border-radius:.375rem}.border{border-width:1px}.border-y{border-top-width:1px}.border-b,.border-y{border-bottom-width:1px}.border-b-2{border-bottom-width:2px}.border-l-2{border-left-width:2px}.border-l-4{border-left-width:4px}.border-t{border-top-width:1px}.border-dotted{border-style:dotted}.border-amber-500\\/70{border-color:#f59e0bb3}.border-amber-600{--tw-border-opacity:1;border-color:rgb(217 119 6/var(--tw-border-opacity))}.border-blue-500{--tw-border-opacity:1;border-color:rgb(59 130 246/var(--tw-border-opacity))}.border-blue-500\\/60{border-color:#3b82f699}.border-gray-100{--tw-border-opacity:1;border-color:rgb(243 244 246/var(--tw-border-opacity))}.border-gray-200{--tw-border-opacity:1;border-color:rgb(229 231 235/var(--tw-border-opacity))}.border-gray-500\\/60{border-color:#6b728099}.border-gray-800{--tw-border-opacity:1;border-color:rgb(31 41 55/var(--tw-border-opacity))}.border-green-500\\/60{border-color:#22c55e99}.border-green-600{--tw-border-opacity:1;border-color:rgb(22 163 74/var(--tw-border-opacity))}.border-orange-500\\/60{border-color:#f9731699}.border-purple-500\\/60{border-color:#a855f799}.border-red-500\\/60{border-color:#ef444499}.border-red-600{--tw-border-opacity:1;border-color:rgb(220 38 38/var(--tw-border-opacity))}.border-slate-400{--tw-border-opacity:1;border-color:rgb(148 163 184/var(--tw-border-opacity))}.border-b-blue-600{--tw-border-opacity:1;border-bottom-color:rgb(37 99 235/var(--tw-border-opacity))}.border-b-gray-100{--tw-border-opacity:1;border-bottom-color:rgb(243 244 246/var(--tw-border-opacity))}.border-l-blue-400{--tw-border-opacity:1;border-left-color:rgb(96 165 250/var(--tw-border-opacity))}.bg-amber-50{--tw-bg-opacity:1;background-color:rgb(255 251 235/var(--tw-bg-opacity))}.bg-amber-50\\/80{background-color:#fffbebcc}.bg-blue-50{--tw-bg-opacity:1;background-color:rgb(239 246 255/var(--tw-bg-opacity))}.bg-blue-50\\/80{background-color:#eff6ffcc}.bg-blue-900{--tw-bg-opacity:1;background-color:rgb(30 58 138/var(--tw-bg-opacity))}.bg-gray-100{--tw-bg-opacity:1;background-color:rgb(243 244 246/var(--tw-bg-opacity))}.bg-gray-50{--tw-bg-opacity:1;background-color:rgb(249 250 251/var(--tw-bg-opacity))}.bg-gray-50\\/10{background-color:#f9fafb1a}.bg-gray-50\\/80{background-color:#f9fafbcc}.bg-green-50{--tw-bg-opacity:1;background-color:rgb(240 253 244/var(--tw-bg-opacity))}.bg-green-50\\/80{background-color:#f0fdf4cc}.bg-orange-50\\/80{background-color:#fff7edcc}.bg-purple-50\\/80{background-color:#faf5ffcc}.bg-red-50{--tw-bg-opacity:1;background-color:rgb(254 242 242/var(--tw-bg-opacity))}.bg-red-50\\/80{background-color:#fef2f2cc}.bg-slate-100{--tw-bg-opacity:1;background-color:rgb(241 245 249/var(--tw-bg-opacity))}.bg-slate-900{--tw-bg-opacity:1;background-color:rgb(15 23 42/var(--tw-bg-opacity))}.bg-stone-200\\/10{background-color:#e7e5e41a}.bg-stone-700{--tw-bg-opacity:1;background-color:rgb(68 64 60/var(--tw-bg-opacity))}.bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255/var(--tw-bg-opacity))}.fill-blue-900{fill:#1e3a8a}.fill-white{fill:#fff}.object-cover{-o-object-fit:cover;object-fit:cover}.object-left{-o-object-position:left;object-position:left}.object-top{-o-object-position:top;object-position:top}.p-1{padding:.25rem}.p-2{padding:.5rem}.p-3{padding:.75rem}.p-4{padding:1rem}.px-1{padding-left:.25rem;padding-right:.25rem}.px-2{padding-left:.5rem;padding-right:.5rem}.px-3{padding-left:.75rem;padding-right:.75rem}.px-4{padding-left:1rem;padding-right:1rem}.px-6{padding-left:1.5rem;padding-right:1.5rem}.py-0{padding-top:0;padding-bottom:0}.py-0\\.5{padding-top:.125rem;padding-bottom:.125rem}.py-1{padding-top:.25rem;padding-bottom:.25rem}.py-2{padding-top:.5rem;padding-bottom:.5rem}.pl-2{padding-left:.5rem}.pl-3{padding-left:.75rem}.pt-3{padding-top:.75rem}.text-right{text-align:right}.align-middle{vertical-align:middle}.text-lg{font-size:1.125rem;line-height:1.75rem}.text-sm{font-size:.875rem;line-height:1.25rem}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-xs{font-size:.75rem;line-height:1rem}.font-bold{font-weight:700}.font-light{font-weight:300}.font-medium{font-weight:500}.font-normal{font-weight:400}.font-semibold{font-weight:600}.font-thin{font-weight:100}.uppercase{text-transform:uppercase}.capitalize{text-transform:capitalize}.italic{font-style:italic}.leading-3{line-height:.75rem}.leading-\\[0\\]{line-height:0}.text-amber-600{--tw-text-opacity:1;color:rgb(217 119 6/var(--tw-text-opacity))}.text-blue-400{--tw-text-opacity:1;color:rgb(96 165 250/var(--tw-text-opacity))}.text-blue-500{--tw-text-opacity:1;color:rgb(59 130 246/var(--tw-text-opacity))}.text-blue-600{--tw-text-opacity:1;color:rgb(37 99 235/var(--tw-text-opacity))}.text-gray-100{--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}.text-gray-500{--tw-text-opacity:1;color:rgb(107 114 128/var(--tw-text-opacity))}.text-gray-600{--tw-text-opacity:1;color:rgb(75 85 99/var(--tw-text-opacity))}.text-green-500{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.text-green-600{--tw-text-opacity:1;color:rgb(22 163 74/var(--tw-text-opacity))}.text-green-700{--tw-text-opacity:1;color:rgb(21 128 61/var(--tw-text-opacity))}.text-inherit{color:inherit}.text-neutral-700{--tw-text-opacity:1;color:rgb(64 64 64/var(--tw-text-opacity))}.text-neutral-900{--tw-text-opacity:1;color:rgb(23 23 23/var(--tw-text-opacity))}.text-orange-600{--tw-text-opacity:1;color:rgb(234 88 12/var(--tw-text-opacity))}.text-purple-600{--tw-text-opacity:1;color:rgb(147 51 234/var(--tw-text-opacity))}.text-purple-700{--tw-text-opacity:1;color:rgb(126 34 206/var(--tw-text-opacity))}.text-red-500{--tw-text-opacity:1;color:rgb(239 68 68/var(--tw-text-opacity))}.text-red-600{--tw-text-opacity:1;color:rgb(220 38 38/var(--tw-text-opacity))}.text-slate-600{--tw-text-opacity:1;color:rgb(71 85 105/var(--tw-text-opacity))}.text-slate-700{--tw-text-opacity:1;color:rgb(51 65 85/var(--tw-text-opacity))}.text-success{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.text-white{--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}.text-yellow-600{--tw-text-opacity:1;color:rgb(202 138 4/var(--tw-text-opacity))}.underline{text-decoration-line:underline}.no-underline{text-decoration-line:none}.opacity-0{opacity:0}.shadow{--tw-shadow:0 1px 3px 0 #0000001a,0 1px 2px -1px #0000001a;--tw-shadow-colored:0 1px 3px 0 var(--tw-shadow-color),0 1px 2px -1px var(--tw-shadow-color)}.shadow,.shadow-md{box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.shadow-md{--tw-shadow:0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;--tw-shadow-colored:0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color)}.shadow-sm{--tw-shadow:0 1px 2px 0 #0000000d;--tw-shadow-colored:0 1px 2px 0 var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.filter{filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)}.transition-opacity{transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.transition-transform{transition-property:transform;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.duration-200{transition-duration:.2s}.ease-in-out{transition-timing-function:cubic-bezier(.4,0,.2,1)}.hover\\:border-blue-500:hover{--tw-border-opacity:1;border-color:rgb(59 130 246/var(--tw-border-opacity))}.hover\\:font-semibold:hover{font-weight:600}.hover\\:text-blue-500:hover{--tw-text-opacity:1;color:rgb(59 130 246/var(--tw-text-opacity))}.hover\\:text-blue-600:hover{--tw-text-opacity:1;color:rgb(37 99 235/var(--tw-text-opacity))}.hover\\:text-gray-700:hover{--tw-text-opacity:1;color:rgb(55 65 81/var(--tw-text-opacity))}.hover\\:text-green-500:hover{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.hover\\:text-inherit:hover{color:inherit}.hover\\:underline:hover{text-decoration-line:underline}.hover\\:no-underline:hover{text-decoration-line:none}.hover\\:opacity-100:hover{opacity:1}.hover\\:shadow-\\[inset_0_0_0px_30px_\\#00000003\\]:hover{--tw-shadow:inset 0 0 0px 30px #00000003;--tw-shadow-colored:inset 0 0 0px 30px var(--tw-shadow-color)}.hover\\:shadow-\\[inset_0_0_0px_30px_\\#00000003\\]:hover,.hover\\:shadow-lg:hover{box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.hover\\:shadow-lg:hover{--tw-shadow:0 10px 15px -3px #0000001a,0 4px 6px -4px #0000001a;--tw-shadow-colored:0 10px 15px -3px var(--tw-shadow-color),0 4px 6px -4px var(--tw-shadow-color)}.hover\\:shadow-md:hover{--tw-shadow:0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;--tw-shadow-colored:0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.active\\:opacity-100:active,.focus\\:opacity-100:focus{opacity:1}.group:hover .group-hover\\:underline{text-decoration-line:underline}.group:hover .group-hover\\:opacity-100{opacity:1}.group:hover .group-hover\\:opacity-70{opacity:.7}:is([data-jp-theme-light=false] .dark\\:border-y-0){border-top-width:0;border-bottom-width:0}:is([data-jp-theme-light=false] .dark\\:border-l-4){border-left-width:4px}:is([data-jp-theme-light=false] .dark\\:border-amber-500\\/70){border-color:#f59e0bb3}:is([data-jp-theme-light=false] .dark\\:border-blue-500\\/60){border-color:#3b82f699}:is([data-jp-theme-light=false] .dark\\:border-gray-500){--tw-border-opacity:1;border-color:rgb(107 114 128/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-gray-500\\/60){border-color:#6b728099}:is([data-jp-theme-light=false] .dark\\:border-gray-800){--tw-border-opacity:1;border-color:rgb(31 41 55/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-green-500\\/60){border-color:#22c55e99}:is([data-jp-theme-light=false] .dark\\:border-orange-500\\/60){border-color:#f9731699}:is([data-jp-theme-light=false] .dark\\:border-purple-500\\/60){border-color:#a855f799}:is([data-jp-theme-light=false] .dark\\:border-red-500\\/60){border-color:#ef444499}:is([data-jp-theme-light=false] .dark\\:border-slate-300){--tw-border-opacity:1;border-color:rgb(203 213 225/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-b-white){--tw-border-opacity:1;border-bottom-color:rgb(255 255 255/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-l-blue-400){--tw-border-opacity:1;border-left-color:rgb(96 165 250/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-600){--tw-bg-opacity:1;background-color:rgb(71 85 105/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-800){--tw-bg-opacity:1;background-color:rgb(30 41 59/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-900){--tw-bg-opacity:1;background-color:rgb(15 23 42/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-stone-700){--tw-bg-opacity:1;background-color:rgb(68 64 60/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-stone-800){--tw-bg-opacity:1;background-color:rgb(41 37 36/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-white){--tw-bg-opacity:1;background-color:rgb(255 255 255/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:fill-white){fill:#fff}:is([data-jp-theme-light=false] .dark\\:text-black){--tw-text-opacity:1;color:rgb(0 0 0/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-100){--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-300){--tw-text-opacity:1;color:rgb(209 213 219/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-400){--tw-text-opacity:1;color:rgb(156 163 175/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-green-500){--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-neutral-200){--tw-text-opacity:1;color:rgb(229 229 229/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-purple-500){--tw-text-opacity:1;color:rgb(168 85 247/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-slate-100){--tw-text-opacity:1;color:rgb(241 245 249/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-white){--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:shadow-2xl){--tw-shadow:0 25px 50px -12px #00000040;--tw-shadow-colored:0 25px 50px -12px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-700){--tw-shadow-color:#404040;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-800){--tw-shadow-color:#262626;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-900){--tw-shadow-color:#171717;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:hover\\:border-blue-400:hover){--tw-border-opacity:1;border-color:rgb(96 165 250/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:text-blue-400:hover){--tw-text-opacity:1;color:rgb(96 165 250/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:text-gray-100:hover){--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:shadow-\\[inset_0_0_0px_30px_\\#FFFFFF03\\]:hover){--tw-shadow:inset 0 0 0px 30px #ffffff03;--tw-shadow-colored:inset 0 0 0px 30px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}@media (min-width:640px){.sm\\:max-w-\\[400px\\]{max-width:400px}.sm\\:max-w-\\[500px\\]{max-width:500px}.sm\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.sm\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.sm\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.sm\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.sm\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.sm\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.sm\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.sm\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.sm\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.sm\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.sm\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.sm\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:768px){.md\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.md\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.md\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.md\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.md\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.md\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.md\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.md\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.md\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.md\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.md\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.md\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:1024px){.lg\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.lg\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.lg\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.lg\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.lg\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.lg\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.lg\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.lg\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.lg\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.lg\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.lg\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.lg\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:1280px){.xl\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.xl\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.xl\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.xl\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.xl\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.xl\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.xl\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.xl\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.xl\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.xl\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.xl\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.xl\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}`, "",{"version":3,"sources":["webpack://./style/app.css"],"names":[],"mappings":"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kB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,CAAC,yBAAyB,iBAAiB,6CAA6C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,CAAC,0BAA0B,iBAAiB,6CAA6C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,CAAC,0BAA0B,iBAAiB,6CAA6C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,kBAAkB,8CAA8C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC,iBAAiB,6CAA6C,CAAC","sourcesContent":[".container{width:100%}@media (min-width:640px){.container{max-width:640px}}@media (min-width:768px){.container{max-width:768px}}@media (min-width:1024px){.container{max-width:1024px}}@media (min-width:1280px){.container{max-width:1280px}}@media (min-width:1536px){.container{max-width:1536px}}.prose{color:var(--tw-prose-body);max-width:65ch}.prose :where(p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:1em;color:var(--jp-content-font-color1);font-family:var(--jp-content-font-family);font-size:var(--jp-content-font-size1);line-height:var(--jp-content-line-height)}.prose :where([class~=lead]):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-lead);font-size:1.25em;line-height:1.6;margin-top:1.2em;margin-bottom:1.2em}.prose :where(a):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--jp-content-link-color,#1976d2);text-decoration:none;font-weight:400}.prose :where(a):not(:where([class~=not-prose],[class~=not-prose] *)):hover{color:var(--jp-content-link-color,#1976d2);text-decoration:underline;font-weight:400}.prose :where(strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-bold);font-weight:600}.prose :where(a strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(blockquote strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(thead th strong):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(ol):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:decimal;margin-top:1.25em;margin-bottom:1.25em;padding-left:1.625em}.prose :where(ol[type=A]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-alpha}.prose :where(ol[type=a]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-alpha}.prose :where(ol[type=A s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-alpha}.prose :where(ol[type=a s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-alpha}.prose :where(ol[type=I]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-roman}.prose :where(ol[type=i]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-roman}.prose :where(ol[type=I s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:upper-roman}.prose :where(ol[type=i s]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:lower-roman}.prose :where(ol[type=\"1\"]):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:decimal}.prose :where(ul):not(:where([class~=not-prose],[class~=not-prose] *)){list-style-type:disc;margin-top:1.25em;margin-bottom:1.25em;padding-left:1.625em}.prose :where(ol>li):not(:where([class~=not-prose],[class~=not-prose] *))::marker{font-weight:400;color:var(--tw-prose-counters)}.prose :where(ul>li):not(:where([class~=not-prose],[class~=not-prose] *))::marker{color:var(--tw-prose-bullets)}.prose :where(dt):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;margin-top:1.25em}.prose :where(hr):not(:where([class~=not-prose],[class~=not-prose] *)){border-color:var(--tw-prose-hr);border-top-width:1px;margin-top:3em;margin-bottom:3em}.prose :where(blockquote):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:500;font-style:italic;color:var(--tw-prose-quotes);border-left-width:.25rem;border-left-color:var(--tw-prose-quote-borders);quotes:\"\\201C\"\"\\201D\"\"\\2018\"\"\\2019\";margin-top:1.6em;margin-bottom:1.6em;padding-left:1em}.prose :where(blockquote p:first-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):before{content:none}.prose :where(blockquote p:last-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:close-quote}.prose :where(h1):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:800;font-size:var(--jp-content-font-size5);margin-top:0;margin-bottom:.8888889em;line-height:1.1111111}.prose :where(h1 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:900;color:inherit}.prose :where(h2):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:700;font-size:var(--jp-content-font-size4);margin-top:2em;margin-bottom:1em;line-height:1.3333333}.prose :where(h2 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:800;color:inherit}.prose :where(h3):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;font-size:var(--jp-content-font-size3);margin-top:1.6em;margin-bottom:.6em;line-height:1.6}.prose :where(h3 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:700;color:inherit}.prose :where(h4):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;margin-top:1.5em;margin-bottom:.5em;line-height:1.5;font-size:var(--jp-content-font-size2)}.prose :where(h4 strong):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:700;color:inherit}.prose :where(img):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(picture):not(:where([class~=not-prose],[class~=not-prose] *)){display:block;margin-top:2em;margin-bottom:2em}.prose :where(kbd):not(:where([class~=not-prose],[class~=not-prose] *)){font-weight:500;font-family:inherit;color:var(--tw-prose-kbd);box-shadow:0 0 0 1px rgb(var(--tw-prose-kbd-shadows)/10%),0 3px 0 rgb(var(--tw-prose-kbd-shadows)/10%);font-size:.875em;border-radius:.3125rem;padding:.1875em .375em}.prose :where(code):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--jp-content-font-color1);font-weight:inherit;font-size:inherit;font-family:var(--jp-code-font-family);line-height:var(--jp-code-line-height);padding:1px 5px;white-space:pre-wrap;background-color:var(--jp-layout-color2)}.prose :where(a code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(h1 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(h2 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit;font-size:.875em}.prose :where(h3 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit;font-size:.9em}.prose :where(h4 code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(blockquote code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(thead th code):not(:where([class~=not-prose],[class~=not-prose] *)){color:inherit}.prose :where(pre):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-pre-code);background-color:var(--tw-prose-pre-bg);overflow-x:auto;font-weight:400;font-size:.875em;line-height:1.7142857;margin-top:1.7142857em;margin-bottom:1.7142857em;border-radius:.375rem;padding:.8571429em 1.1428571em}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)){background-color:initial;border-width:0;border-radius:0;padding:0;font-weight:inherit;color:inherit;font-size:inherit;font-family:inherit;line-height:inherit}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)):before{content:none}.prose :where(pre code):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:none}.prose :where(table):not(:where([class~=not-prose],[class~=not-prose] *)){width:100%;table-layout:auto;text-align:left;margin-top:2em;margin-bottom:2em;font-size:.875em;line-height:1.7142857}.prose :where(thead):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:1px;border-bottom-color:var(--tw-prose-th-borders)}.prose :where(thead th):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-headings);font-weight:600;vertical-align:bottom;padding-right:.5714286em;padding-bottom:.5714286em;padding-left:.5714286em}.prose :where(tbody tr):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:1px;border-bottom-color:var(--tw-prose-td-borders)}.prose :where(tbody tr:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){border-bottom-width:0}.prose :where(tbody td):not(:where([class~=not-prose],[class~=not-prose] *)){vertical-align:initial}.prose :where(tfoot):not(:where([class~=not-prose],[class~=not-prose] *)){border-top-width:1px;border-top-color:var(--tw-prose-th-borders)}.prose :where(tfoot td):not(:where([class~=not-prose],[class~=not-prose] *)){vertical-align:top}.prose :where(figure>*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:0}.prose :where(figcaption):not(:where([class~=not-prose],[class~=not-prose] *)){color:var(--tw-prose-captions);font-size:.875em;line-height:1.4285714;margin-top:.8571429em}.prose{--tw-prose-body:#374151;--tw-prose-headings:#111827;--tw-prose-lead:#4b5563;--tw-prose-links:#111827;--tw-prose-bold:#111827;--tw-prose-counters:#6b7280;--tw-prose-bullets:#d1d5db;--tw-prose-hr:#e5e7eb;--tw-prose-quotes:#111827;--tw-prose-quote-borders:#e5e7eb;--tw-prose-captions:#6b7280;--tw-prose-kbd:#111827;--tw-prose-kbd-shadows:17 24 39;--tw-prose-code:#111827;--tw-prose-pre-code:#e5e7eb;--tw-prose-pre-bg:#1f2937;--tw-prose-th-borders:#d1d5db;--tw-prose-td-borders:#e5e7eb;--tw-prose-invert-body:#d1d5db;--tw-prose-invert-headings:#fff;--tw-prose-invert-lead:#9ca3af;--tw-prose-invert-links:#fff;--tw-prose-invert-bold:#fff;--tw-prose-invert-counters:#9ca3af;--tw-prose-invert-bullets:#4b5563;--tw-prose-invert-hr:#374151;--tw-prose-invert-quotes:#f3f4f6;--tw-prose-invert-quote-borders:#374151;--tw-prose-invert-captions:#9ca3af;--tw-prose-invert-kbd:#fff;--tw-prose-invert-kbd-shadows:255 255 255;--tw-prose-invert-code:#fff;--tw-prose-invert-pre-code:#d1d5db;--tw-prose-invert-pre-bg:#00000080;--tw-prose-invert-th-borders:#4b5563;--tw-prose-invert-td-borders:#374151;font-size:1rem;line-height:1.75}.prose :where(picture>img):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0;margin-bottom:0}.prose :where(video):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(li):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.25rem;margin-bottom:.25rem}.prose :where(ol>li):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:.375em}.prose :where(ul>li):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:.375em}.prose :where(.prose>ul>li p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.75em;margin-bottom:.75em}.prose :where(.prose>ul>li>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em}.prose :where(.prose>ul>li>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:1.25em}.prose :where(.prose>ol>li>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em}.prose :where(.prose>ol>li>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:1.25em}.prose :where(ul ul,ul ol,ol ul,ol ol):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.75em;margin-bottom:.75em}.prose :where(dl):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:1.25em;margin-bottom:1.25em}.prose :where(dd):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.5em;padding-left:1.625em}.prose :where(hr+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h2+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h3+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(h4+*):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(thead th:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:0}.prose :where(thead th:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-right:0}.prose :where(tbody td,tfoot td):not(:where([class~=not-prose],[class~=not-prose] *)){padding:.5714286em}.prose :where(tbody td:first-child,tfoot td:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-left:0}.prose :where(tbody td:last-child,tfoot td:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){padding-right:0}.prose :where(figure):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:2em;margin-bottom:2em}.prose :where(.prose>:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:0}.prose :where(.prose>:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:0}.prose :where(h1,h2,h3,h4,h5,h6):not(:where([class~=not-prose],[class~=not-prose] *)){line-height:var(--jp-content-heading-line-height,1);font-weight:var(--jp-content-heading-font-weight,500);font-style:normal;margin-top:var(--jp-content-heading-margin-top,1.2em);margin-bottom:var(--jp-content-heading-margin-bottom,.8em);color:var(--jp-content-font-color1)}.prose :where(h1:first-child,h2:first-child,h3:first-child,h4:first-child,h5:first-child,h6:first-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:calc(var(--jp-content-heading-margin-top)*.5)}.prose :where(h1:last-child,h2:last-child,h3:last-child,h4:last-child,h5:last-child,h6:last-child):not(:where([class~=not-prose],[class~=not-prose] *)){margin-bottom:calc(var(--jp-content-heading-margin-bottom)*.5)}.prose :where(h5):not(:where([class~=not-prose],[class~=not-prose] *)){font-size:var(--jp-content-font-size1)}.prose :where(h6):not(:where([class~=not-prose],[class~=not-prose] *)){font-size:var(--jp-content-font-size0)}.prose :where(blockquote p:first-of-type):not(:where([class~=not-prose],[class~=not-prose] *)):after{content:none}.prose :where(li>p,dd>p,header>p,footer>p):not(:where([class~=not-prose],[class~=not-prose] *)){margin-top:.25rem;margin-bottom:.25rem}.static{position:static}.absolute{position:absolute}.relative{position:relative}.right-1{right:.25rem}.top-1{top:.25rem}.top-\\[32px\\]{top:32px}.float-right{float:right}.m-0{margin:0}.my-2{margin-top:.5rem;margin-bottom:.5rem}.my-5{margin-top:1.25rem;margin-bottom:1.25rem}.mb-4{margin-bottom:1rem}.ml-1{margin-left:.25rem}.ml-2{margin-left:.5rem}.ml-3{margin-left:.75rem}.ml-4{margin-left:1rem}.mr-1{margin-right:.25rem}.mr-2{margin-right:.5rem}.mr-3{margin-right:.75rem}.mt-2{margin-top:.5rem}.mt-3{margin-top:.75rem}.block{display:block}.inline-block{display:inline-block}.inline{display:inline}.flex{display:flex}.inline-flex{display:inline-flex}.table{display:table}.grid{display:grid}.hidden{display:none}.h-4{height:1rem}.h-\\[10px\\]{height:10px}.h-\\[150px\\]{height:150px}.h-full{height:100%}.max-h-\\[300px\\]{max-height:300px}.max-h-\\[4rem\\]{max-height:4rem}.min-h-\\[2em\\]{min-height:2em}.w-4{width:1rem}.w-\\[10px\\]{width:10px}.w-\\[300px\\]{width:300px}.w-\\[400px\\]{width:400px}.w-\\[500px\\]{width:500px}.w-full{width:100%}.min-w-0{min-width:0}.max-w-\\[80vw\\]{max-width:80vw}.flex-1{flex:1 1 0%}.flex-none{flex:none}.flex-grow,.grow{flex-grow:1}.-translate-y-\\[1px\\],.-translate-y-px{--tw-translate-y:-1px}.-translate-y-\\[1px\\],.-translate-y-px,.translate-y-2{transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.translate-y-2{--tw-translate-y:0.5rem}.transform{transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}@keyframes pulse{50%{opacity:.5}}.animate-pulse{animation:pulse 2s cubic-bezier(.4,0,.6,1) infinite}.cursor-help{cursor:help}.cursor-pointer{cursor:pointer}.select-none{-webkit-user-select:none;-moz-user-select:none;user-select:none}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}.flex-row{flex-direction:row}.flex-col{flex-direction:column}.flex-wrap{flex-wrap:wrap}.items-center{align-items:center}.gap-4{gap:1rem}.self-center{align-self:center}.overflow-auto{overflow:auto}.overflow-hidden{overflow:hidden}.overflow-x-auto{overflow-x:auto}.overflow-y-hidden{overflow-y:hidden}.break-words{overflow-wrap:break-word}.rounded{border-radius:.25rem}.rounded-full{border-radius:9999px}.rounded-md{border-radius:.375rem}.border{border-width:1px}.border-y{border-top-width:1px}.border-b,.border-y{border-bottom-width:1px}.border-b-2{border-bottom-width:2px}.border-l-2{border-left-width:2px}.border-l-4{border-left-width:4px}.border-t{border-top-width:1px}.border-dotted{border-style:dotted}.border-amber-500\\/70{border-color:#f59e0bb3}.border-amber-600{--tw-border-opacity:1;border-color:rgb(217 119 6/var(--tw-border-opacity))}.border-blue-500{--tw-border-opacity:1;border-color:rgb(59 130 246/var(--tw-border-opacity))}.border-blue-500\\/60{border-color:#3b82f699}.border-gray-100{--tw-border-opacity:1;border-color:rgb(243 244 246/var(--tw-border-opacity))}.border-gray-200{--tw-border-opacity:1;border-color:rgb(229 231 235/var(--tw-border-opacity))}.border-gray-500\\/60{border-color:#6b728099}.border-gray-800{--tw-border-opacity:1;border-color:rgb(31 41 55/var(--tw-border-opacity))}.border-green-500\\/60{border-color:#22c55e99}.border-green-600{--tw-border-opacity:1;border-color:rgb(22 163 74/var(--tw-border-opacity))}.border-orange-500\\/60{border-color:#f9731699}.border-purple-500\\/60{border-color:#a855f799}.border-red-500\\/60{border-color:#ef444499}.border-red-600{--tw-border-opacity:1;border-color:rgb(220 38 38/var(--tw-border-opacity))}.border-slate-400{--tw-border-opacity:1;border-color:rgb(148 163 184/var(--tw-border-opacity))}.border-b-blue-600{--tw-border-opacity:1;border-bottom-color:rgb(37 99 235/var(--tw-border-opacity))}.border-b-gray-100{--tw-border-opacity:1;border-bottom-color:rgb(243 244 246/var(--tw-border-opacity))}.border-l-blue-400{--tw-border-opacity:1;border-left-color:rgb(96 165 250/var(--tw-border-opacity))}.bg-amber-50{--tw-bg-opacity:1;background-color:rgb(255 251 235/var(--tw-bg-opacity))}.bg-amber-50\\/80{background-color:#fffbebcc}.bg-blue-50{--tw-bg-opacity:1;background-color:rgb(239 246 255/var(--tw-bg-opacity))}.bg-blue-50\\/80{background-color:#eff6ffcc}.bg-blue-900{--tw-bg-opacity:1;background-color:rgb(30 58 138/var(--tw-bg-opacity))}.bg-gray-100{--tw-bg-opacity:1;background-color:rgb(243 244 246/var(--tw-bg-opacity))}.bg-gray-50{--tw-bg-opacity:1;background-color:rgb(249 250 251/var(--tw-bg-opacity))}.bg-gray-50\\/10{background-color:#f9fafb1a}.bg-gray-50\\/80{background-color:#f9fafbcc}.bg-green-50{--tw-bg-opacity:1;background-color:rgb(240 253 244/var(--tw-bg-opacity))}.bg-green-50\\/80{background-color:#f0fdf4cc}.bg-orange-50\\/80{background-color:#fff7edcc}.bg-purple-50\\/80{background-color:#faf5ffcc}.bg-red-50{--tw-bg-opacity:1;background-color:rgb(254 242 242/var(--tw-bg-opacity))}.bg-red-50\\/80{background-color:#fef2f2cc}.bg-slate-100{--tw-bg-opacity:1;background-color:rgb(241 245 249/var(--tw-bg-opacity))}.bg-slate-900{--tw-bg-opacity:1;background-color:rgb(15 23 42/var(--tw-bg-opacity))}.bg-stone-200\\/10{background-color:#e7e5e41a}.bg-stone-700{--tw-bg-opacity:1;background-color:rgb(68 64 60/var(--tw-bg-opacity))}.bg-white{--tw-bg-opacity:1;background-color:rgb(255 255 255/var(--tw-bg-opacity))}.fill-blue-900{fill:#1e3a8a}.fill-white{fill:#fff}.object-cover{-o-object-fit:cover;object-fit:cover}.object-left{-o-object-position:left;object-position:left}.object-top{-o-object-position:top;object-position:top}.p-1{padding:.25rem}.p-2{padding:.5rem}.p-3{padding:.75rem}.p-4{padding:1rem}.px-1{padding-left:.25rem;padding-right:.25rem}.px-2{padding-left:.5rem;padding-right:.5rem}.px-3{padding-left:.75rem;padding-right:.75rem}.px-4{padding-left:1rem;padding-right:1rem}.px-6{padding-left:1.5rem;padding-right:1.5rem}.py-0{padding-top:0;padding-bottom:0}.py-0\\.5{padding-top:.125rem;padding-bottom:.125rem}.py-1{padding-top:.25rem;padding-bottom:.25rem}.py-2{padding-top:.5rem;padding-bottom:.5rem}.pl-2{padding-left:.5rem}.pl-3{padding-left:.75rem}.pt-3{padding-top:.75rem}.text-right{text-align:right}.align-middle{vertical-align:middle}.text-lg{font-size:1.125rem;line-height:1.75rem}.text-sm{font-size:.875rem;line-height:1.25rem}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-xs{font-size:.75rem;line-height:1rem}.font-bold{font-weight:700}.font-light{font-weight:300}.font-medium{font-weight:500}.font-normal{font-weight:400}.font-semibold{font-weight:600}.font-thin{font-weight:100}.uppercase{text-transform:uppercase}.capitalize{text-transform:capitalize}.italic{font-style:italic}.leading-3{line-height:.75rem}.leading-\\[0\\]{line-height:0}.text-amber-600{--tw-text-opacity:1;color:rgb(217 119 6/var(--tw-text-opacity))}.text-blue-400{--tw-text-opacity:1;color:rgb(96 165 250/var(--tw-text-opacity))}.text-blue-500{--tw-text-opacity:1;color:rgb(59 130 246/var(--tw-text-opacity))}.text-blue-600{--tw-text-opacity:1;color:rgb(37 99 235/var(--tw-text-opacity))}.text-gray-100{--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}.text-gray-500{--tw-text-opacity:1;color:rgb(107 114 128/var(--tw-text-opacity))}.text-gray-600{--tw-text-opacity:1;color:rgb(75 85 99/var(--tw-text-opacity))}.text-green-500{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.text-green-600{--tw-text-opacity:1;color:rgb(22 163 74/var(--tw-text-opacity))}.text-green-700{--tw-text-opacity:1;color:rgb(21 128 61/var(--tw-text-opacity))}.text-inherit{color:inherit}.text-neutral-700{--tw-text-opacity:1;color:rgb(64 64 64/var(--tw-text-opacity))}.text-neutral-900{--tw-text-opacity:1;color:rgb(23 23 23/var(--tw-text-opacity))}.text-orange-600{--tw-text-opacity:1;color:rgb(234 88 12/var(--tw-text-opacity))}.text-purple-600{--tw-text-opacity:1;color:rgb(147 51 234/var(--tw-text-opacity))}.text-purple-700{--tw-text-opacity:1;color:rgb(126 34 206/var(--tw-text-opacity))}.text-red-500{--tw-text-opacity:1;color:rgb(239 68 68/var(--tw-text-opacity))}.text-red-600{--tw-text-opacity:1;color:rgb(220 38 38/var(--tw-text-opacity))}.text-slate-600{--tw-text-opacity:1;color:rgb(71 85 105/var(--tw-text-opacity))}.text-slate-700{--tw-text-opacity:1;color:rgb(51 65 85/var(--tw-text-opacity))}.text-success{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.text-white{--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}.text-yellow-600{--tw-text-opacity:1;color:rgb(202 138 4/var(--tw-text-opacity))}.underline{text-decoration-line:underline}.no-underline{text-decoration-line:none}.opacity-0{opacity:0}.shadow{--tw-shadow:0 1px 3px 0 #0000001a,0 1px 2px -1px #0000001a;--tw-shadow-colored:0 1px 3px 0 var(--tw-shadow-color),0 1px 2px -1px var(--tw-shadow-color)}.shadow,.shadow-md{box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.shadow-md{--tw-shadow:0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;--tw-shadow-colored:0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color)}.shadow-sm{--tw-shadow:0 1px 2px 0 #0000000d;--tw-shadow-colored:0 1px 2px 0 var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.filter{filter:var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)}.transition-opacity{transition-property:opacity;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.transition-transform{transition-property:transform;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.duration-200{transition-duration:.2s}.ease-in-out{transition-timing-function:cubic-bezier(.4,0,.2,1)}.hover\\:border-blue-500:hover{--tw-border-opacity:1;border-color:rgb(59 130 246/var(--tw-border-opacity))}.hover\\:font-semibold:hover{font-weight:600}.hover\\:text-blue-500:hover{--tw-text-opacity:1;color:rgb(59 130 246/var(--tw-text-opacity))}.hover\\:text-blue-600:hover{--tw-text-opacity:1;color:rgb(37 99 235/var(--tw-text-opacity))}.hover\\:text-gray-700:hover{--tw-text-opacity:1;color:rgb(55 65 81/var(--tw-text-opacity))}.hover\\:text-green-500:hover{--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}.hover\\:text-inherit:hover{color:inherit}.hover\\:underline:hover{text-decoration-line:underline}.hover\\:no-underline:hover{text-decoration-line:none}.hover\\:opacity-100:hover{opacity:1}.hover\\:shadow-\\[inset_0_0_0px_30px_\\#00000003\\]:hover{--tw-shadow:inset 0 0 0px 30px #00000003;--tw-shadow-colored:inset 0 0 0px 30px var(--tw-shadow-color)}.hover\\:shadow-\\[inset_0_0_0px_30px_\\#00000003\\]:hover,.hover\\:shadow-lg:hover{box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.hover\\:shadow-lg:hover{--tw-shadow:0 10px 15px -3px #0000001a,0 4px 6px -4px #0000001a;--tw-shadow-colored:0 10px 15px -3px var(--tw-shadow-color),0 4px 6px -4px var(--tw-shadow-color)}.hover\\:shadow-md:hover{--tw-shadow:0 4px 6px -1px #0000001a,0 2px 4px -2px #0000001a;--tw-shadow-colored:0 4px 6px -1px var(--tw-shadow-color),0 2px 4px -2px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.active\\:opacity-100:active,.focus\\:opacity-100:focus{opacity:1}.group:hover .group-hover\\:underline{text-decoration-line:underline}.group:hover .group-hover\\:opacity-100{opacity:1}.group:hover .group-hover\\:opacity-70{opacity:.7}:is([data-jp-theme-light=false] .dark\\:border-y-0){border-top-width:0;border-bottom-width:0}:is([data-jp-theme-light=false] .dark\\:border-l-4){border-left-width:4px}:is([data-jp-theme-light=false] .dark\\:border-amber-500\\/70){border-color:#f59e0bb3}:is([data-jp-theme-light=false] .dark\\:border-blue-500\\/60){border-color:#3b82f699}:is([data-jp-theme-light=false] .dark\\:border-gray-500){--tw-border-opacity:1;border-color:rgb(107 114 128/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-gray-500\\/60){border-color:#6b728099}:is([data-jp-theme-light=false] .dark\\:border-gray-800){--tw-border-opacity:1;border-color:rgb(31 41 55/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-green-500\\/60){border-color:#22c55e99}:is([data-jp-theme-light=false] .dark\\:border-orange-500\\/60){border-color:#f9731699}:is([data-jp-theme-light=false] .dark\\:border-purple-500\\/60){border-color:#a855f799}:is([data-jp-theme-light=false] .dark\\:border-red-500\\/60){border-color:#ef444499}:is([data-jp-theme-light=false] .dark\\:border-slate-300){--tw-border-opacity:1;border-color:rgb(203 213 225/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-b-white){--tw-border-opacity:1;border-bottom-color:rgb(255 255 255/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:border-l-blue-400){--tw-border-opacity:1;border-left-color:rgb(96 165 250/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-600){--tw-bg-opacity:1;background-color:rgb(71 85 105/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-800){--tw-bg-opacity:1;background-color:rgb(30 41 59/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-slate-900){--tw-bg-opacity:1;background-color:rgb(15 23 42/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-stone-700){--tw-bg-opacity:1;background-color:rgb(68 64 60/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-stone-800){--tw-bg-opacity:1;background-color:rgb(41 37 36/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:bg-white){--tw-bg-opacity:1;background-color:rgb(255 255 255/var(--tw-bg-opacity))}:is([data-jp-theme-light=false] .dark\\:fill-white){fill:#fff}:is([data-jp-theme-light=false] .dark\\:text-black){--tw-text-opacity:1;color:rgb(0 0 0/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-100){--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-300){--tw-text-opacity:1;color:rgb(209 213 219/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-gray-400){--tw-text-opacity:1;color:rgb(156 163 175/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-green-500){--tw-text-opacity:1;color:rgb(34 197 94/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-neutral-200){--tw-text-opacity:1;color:rgb(229 229 229/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-purple-500){--tw-text-opacity:1;color:rgb(168 85 247/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-slate-100){--tw-text-opacity:1;color:rgb(241 245 249/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:text-white){--tw-text-opacity:1;color:rgb(255 255 255/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:shadow-2xl){--tw-shadow:0 25px 50px -12px #00000040;--tw-shadow-colored:0 25px 50px -12px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-700){--tw-shadow-color:#404040;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-800){--tw-shadow-color:#262626;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:shadow-neutral-900){--tw-shadow-color:#171717;--tw-shadow:var(--tw-shadow-colored)}:is([data-jp-theme-light=false] .dark\\:hover\\:border-blue-400:hover){--tw-border-opacity:1;border-color:rgb(96 165 250/var(--tw-border-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:text-blue-400:hover){--tw-text-opacity:1;color:rgb(96 165 250/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:text-gray-100:hover){--tw-text-opacity:1;color:rgb(243 244 246/var(--tw-text-opacity))}:is([data-jp-theme-light=false] .dark\\:hover\\:shadow-\\[inset_0_0_0px_30px_\\#FFFFFF03\\]:hover){--tw-shadow:inset 0 0 0px 30px #ffffff03;--tw-shadow-colored:inset 0 0 0px 30px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}@media (min-width:640px){.sm\\:max-w-\\[400px\\]{max-width:400px}.sm\\:max-w-\\[500px\\]{max-width:500px}.sm\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.sm\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.sm\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.sm\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.sm\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.sm\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.sm\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.sm\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.sm\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.sm\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.sm\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.sm\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:768px){.md\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.md\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.md\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.md\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.md\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.md\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.md\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.md\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.md\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.md\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.md\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.md\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:1024px){.lg\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.lg\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.lg\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.lg\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.lg\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.lg\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.lg\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.lg\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.lg\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.lg\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.lg\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.lg\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}@media (min-width:1280px){.xl\\:grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.xl\\:grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.xl\\:grid-cols-11{grid-template-columns:repeat(11,minmax(0,1fr))}.xl\\:grid-cols-12{grid-template-columns:repeat(12,minmax(0,1fr))}.xl\\:grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.xl\\:grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.xl\\:grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.xl\\:grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.xl\\:grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.xl\\:grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.xl\\:grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.xl\\:grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}}"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./style/base.css":
/*!**************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/base.css ***!
  \**************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/sourceMaps.js */ "./node_modules/css-loader/dist/runtime/sourceMaps.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_app_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! -!../node_modules/css-loader/dist/cjs.js!./app.css */ "./node_modules/css-loader/dist/cjs.js!./style/app.css");
// Imports



var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_sourceMaps_js__WEBPACK_IMPORTED_MODULE_0___default()));
___CSS_LOADER_EXPORT___.i(_node_modules_css_loader_dist_cjs_js_app_css__WEBPACK_IMPORTED_MODULE_2__["default"]);
// Module
___CSS_LOADER_EXPORT___.push([module.id, `/*
    See the JupyterLab Developer Guide for useful CSS Patterns:

    https://jupyterlab.readthedocs.io/en/stable/developer/css.html
*/

div#papyri-browser {
  padding: 15px;
}

code {
  color: #db2777;
  font-weight: 400;
  font-size: 0.875em;
}

.not-implemented {
  border: 1px solid orange;
}

div#papyri-browser a:hover {
  text-decoration: underline;
}

#papyri-browser a {
  font-weight: bold;
}

#papyri-browser .view {
  overflow: scroll;
  height: 100%;
}

#papyri-browser {
  & span.signature-separator {
    white-space: pre;
  }

  & span.default-value {
    opacity: 30%;
  }
  & span.type-ann,
  & span.ret-ann {
    opacity: 30%;
    color: gray;
  }

  & span.param-block {
    white-space: pre;
  }
}
`, "",{"version":3,"sources":["webpack://./style/base.css"],"names":[],"mappings":"AAAA;;;;CAIC;;AAGD;EACE,aAAa;AACf;;AAEA;EACE,cAAc;EACd,gBAAgB;EAChB,kBAAkB;AACpB;;AAEA;EACE,wBAAwB;AAC1B;;AAEA;EACE,0BAA0B;AAC5B;;AAEA;EACE,iBAAiB;AACnB;;AAEA;EACE,gBAAgB;EAChB,YAAY;AACd;;AAEA;EACE;IACE,gBAAgB;EAClB;;EAEA;IACE,YAAY;EACd;EACA;;IAEE,YAAY;IACZ,WAAW;EACb;;EAEA;IACE,gBAAgB;EAClB;AACF","sourcesContent":["/*\n    See the JupyterLab Developer Guide for useful CSS Patterns:\n\n    https://jupyterlab.readthedocs.io/en/stable/developer/css.html\n*/\n@import 'app.css';\n\ndiv#papyri-browser {\n  padding: 15px;\n}\n\ncode {\n  color: #db2777;\n  font-weight: 400;\n  font-size: 0.875em;\n}\n\n.not-implemented {\n  border: 1px solid orange;\n}\n\ndiv#papyri-browser a:hover {\n  text-decoration: underline;\n}\n\n#papyri-browser a {\n  font-weight: bold;\n}\n\n#papyri-browser .view {\n  overflow: scroll;\n  height: 100%;\n}\n\n#papyri-browser {\n  & span.signature-separator {\n    white-space: pre;\n  }\n\n  & span.default-value {\n    opacity: 30%;\n  }\n  & span.type-ann,\n  & span.ret-ann {\n    opacity: 30%;\n    color: gray;\n  }\n\n  & span.param-block {\n    white-space: pre;\n  }\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./style/base.css":
/*!************************!*\
  !*** ./style/base.css ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleDomAPI.js */ "./node_modules/style-loader/dist/runtime/styleDomAPI.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertBySelector.js */ "./node_modules/style-loader/dist/runtime/insertBySelector.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js */ "./node_modules/style-loader/dist/runtime/setAttributesWithoutAttributes.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/insertStyleElement.js */ "./node_modules/style-loader/dist/runtime/insertStyleElement.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/styleTagTransform.js */ "./node_modules/style-loader/dist/runtime/styleTagTransform.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./base.css */ "./node_modules/css-loader/dist/cjs.js!./style/base.css");

      
      
      
      
      
      
      
      
      

var options = {};

options.styleTagTransform = (_node_modules_style_loader_dist_runtime_styleTagTransform_js__WEBPACK_IMPORTED_MODULE_5___default());
options.setAttributes = (_node_modules_style_loader_dist_runtime_setAttributesWithoutAttributes_js__WEBPACK_IMPORTED_MODULE_3___default());

      options.insert = _node_modules_style_loader_dist_runtime_insertBySelector_js__WEBPACK_IMPORTED_MODULE_2___default().bind(null, "head");
    
options.domAPI = (_node_modules_style_loader_dist_runtime_styleDomAPI_js__WEBPACK_IMPORTED_MODULE_1___default());
options.insertStyleElement = (_node_modules_style_loader_dist_runtime_insertStyleElement_js__WEBPACK_IMPORTED_MODULE_4___default());

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"], options);




       /* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"] && _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals ? _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_6__["default"].locals : undefined);


/***/ })

}]);
//# sourceMappingURL=style_index_js.6678ae9fe4e19286b970.js.map