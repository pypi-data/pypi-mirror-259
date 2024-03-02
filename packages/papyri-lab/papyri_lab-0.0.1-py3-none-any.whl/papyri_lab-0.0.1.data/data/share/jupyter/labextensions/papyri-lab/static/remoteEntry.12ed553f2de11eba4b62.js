var _JUPYTERLAB;
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "webpack/container/entry/papyri-lab":
/*!***********************!*\
  !*** container entry ***!
  \***********************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

var moduleMap = {
	"./index": () => {
		return Promise.all([__webpack_require__.e("vendors-node_modules_myst-theme_providers_dist_index_js"), __webpack_require__.e("webpack_sharing_consume_default_react"), __webpack_require__.e("lib_index_js")]).then(() => (() => ((__webpack_require__(/*! ./lib/index.js */ "./lib/index.js")))));
	},
	"./extension": () => {
		return Promise.all([__webpack_require__.e("vendors-node_modules_myst-theme_providers_dist_index_js"), __webpack_require__.e("webpack_sharing_consume_default_react"), __webpack_require__.e("lib_index_js")]).then(() => (() => ((__webpack_require__(/*! ./lib/index.js */ "./lib/index.js")))));
	},
	"./style": () => {
		return __webpack_require__.e("style_index_js").then(() => (() => ((__webpack_require__(/*! ./style/index.js */ "./style/index.js")))));
	}
};
var get = (module, getScope) => {
	__webpack_require__.R = getScope;
	getScope = (
		__webpack_require__.o(moduleMap, module)
			? moduleMap[module]()
			: Promise.resolve().then(() => {
				throw new Error('Module "' + module + '" does not exist in container.');
			})
	);
	__webpack_require__.R = undefined;
	return getScope;
};
var init = (shareScope, initScope) => {
	if (!__webpack_require__.S) return;
	var name = "default"
	var oldScope = __webpack_require__.S[name];
	if(oldScope && oldScope !== shareScope) throw new Error("Container initialization failed as it has already been initialized with a different share scope");
	__webpack_require__.S[name] = shareScope;
	return __webpack_require__.I(name, initScope);
};

// This exports getters to disallow modifications
__webpack_require__.d(exports, {
	get: () => (get),
	init: () => (init)
});

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			id: moduleId,
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = __webpack_modules__;
/******/ 	
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = __webpack_module_cache__;
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/create fake namespace object */
/******/ 	(() => {
/******/ 		var getProto = Object.getPrototypeOf ? (obj) => (Object.getPrototypeOf(obj)) : (obj) => (obj.__proto__);
/******/ 		var leafPrototypes;
/******/ 		// create a fake namespace object
/******/ 		// mode & 1: value is a module id, require it
/******/ 		// mode & 2: merge all properties of value into the ns
/******/ 		// mode & 4: return value when already ns object
/******/ 		// mode & 16: return value when it's Promise-like
/******/ 		// mode & 8|1: behave like require
/******/ 		__webpack_require__.t = function(value, mode) {
/******/ 			if(mode & 1) value = this(value);
/******/ 			if(mode & 8) return value;
/******/ 			if(typeof value === 'object' && value) {
/******/ 				if((mode & 4) && value.__esModule) return value;
/******/ 				if((mode & 16) && typeof value.then === 'function') return value;
/******/ 			}
/******/ 			var ns = Object.create(null);
/******/ 			__webpack_require__.r(ns);
/******/ 			var def = {};
/******/ 			leafPrototypes = leafPrototypes || [null, getProto({}), getProto([]), getProto(getProto)];
/******/ 			for(var current = mode & 2 && value; typeof current == 'object' && !~leafPrototypes.indexOf(current); current = getProto(current)) {
/******/ 				Object.getOwnPropertyNames(current).forEach((key) => (def[key] = () => (value[key])));
/******/ 			}
/******/ 			def['default'] = () => (value);
/******/ 			__webpack_require__.d(ns, def);
/******/ 			return ns;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/ensure chunk */
/******/ 	(() => {
/******/ 		__webpack_require__.f = {};
/******/ 		// This file contains only the entry chunk.
/******/ 		// The chunk loading function for additional chunks
/******/ 		__webpack_require__.e = (chunkId) => {
/******/ 			return Promise.all(Object.keys(__webpack_require__.f).reduce((promises, key) => {
/******/ 				__webpack_require__.f[key](chunkId, promises);
/******/ 				return promises;
/******/ 			}, []));
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/get javascript chunk filename */
/******/ 	(() => {
/******/ 		// This function allow to reference async chunks
/******/ 		__webpack_require__.u = (chunkId) => {
/******/ 			// return url for filenames based on template
/******/ 			return "" + chunkId + "." + {"vendors-node_modules_myst-theme_providers_dist_index_js":"7d0621e36a58e9b558d7","webpack_sharing_consume_default_react":"f97fbec7f2a44e0c3d5e","lib_index_js":"454e946da84f62827b00","style_index_js":"6678ae9fe4e19286b970","vendors-node_modules_myst-to-react_dist_index_js":"b4adb8f170cfce9439dc","webpack_sharing_consume_default_react-dom":"78bb5cde756bc9d2d9a0","react-syntax-highlighter/lowlight-import":"e6cfed2736bb48b174d8","react-syntax-highlighter_languages_highlight_oneC":"f4822b3c37957d390f58","react-syntax-highlighter_languages_highlight_abnf":"c75ea3a3197827dba6de","react-syntax-highlighter_languages_highlight_accesslog":"79ae5c1f1662db990aec","react-syntax-highlighter_languages_highlight_actionscript":"d88c82655beec0c55580","react-syntax-highlighter_languages_highlight_ada":"0f21e543e389fab2eb74","react-syntax-highlighter_languages_highlight_angelscript":"a5c27c65aab6cab94f2c","react-syntax-highlighter_languages_highlight_apache":"5c9b53a46cd4f2c341d7","react-syntax-highlighter_languages_highlight_applescript":"24c38a334aa3eb1459aa","react-syntax-highlighter_languages_highlight_arcade":"07fe25a500436af193cd","react-syntax-highlighter_languages_highlight_arduino":"b74333d8d0daf378aff4","react-syntax-highlighter_languages_highlight_armasm":"33691c6fe46da2f5ea6f","react-syntax-highlighter_languages_highlight_asciidoc":"46c7cc5b1c8f9d549931","react-syntax-highlighter_languages_highlight_aspectj":"6c2d07ed3f93d969fca9","react-syntax-highlighter_languages_highlight_autohotkey":"e85403bbde942e776fad","react-syntax-highlighter_languages_highlight_autoit":"0d494dfedd08a7bcdb78","react-syntax-highlighter_languages_highlight_avrasm":"457fe42b1c735f20d1f9","react-syntax-highlighter_languages_highlight_awk":"2d6aaf399f5b66ba6825","react-syntax-highlighter_languages_highlight_axapta":"71972cbc4272ef8d6610","react-syntax-highlighter_languages_highlight_bash":"b3f69c843d079fd5757a","react-syntax-highlighter_languages_highlight_basic":"dc8a3696b82da8c89284","react-syntax-highlighter_languages_highlight_bnf":"07bfa989fd95577fae06","react-syntax-highlighter_languages_highlight_brainfuck":"c56efeb76b0531e196f3","react-syntax-highlighter_languages_highlight_cLike":"b33a0750b6db049bf31a","react-syntax-highlighter_languages_highlight_c":"a94f52f8a541adb877a3","react-syntax-highlighter_languages_highlight_cal":"4fb12efba18a09955015","react-syntax-highlighter_languages_highlight_capnproto":"d5e19a077218648e1e20","react-syntax-highlighter_languages_highlight_ceylon":"130a9b9fa86c8632bbf0","react-syntax-highlighter_languages_highlight_clean":"3d39b6f608f9901feda3","react-syntax-highlighter_languages_highlight_clojureRepl":"ba07c7c372db5e5ffc96","react-syntax-highlighter_languages_highlight_clojure":"14329fc144e1ec500a13","react-syntax-highlighter_languages_highlight_cmake":"c451a88c7c936e389dc3","react-syntax-highlighter_languages_highlight_coffeescript":"68d88fe35ee8e804597f","react-syntax-highlighter_languages_highlight_coq":"baa50836fa666e6af8f1","react-syntax-highlighter_languages_highlight_cos":"fda1a735518d05d01449","react-syntax-highlighter_languages_highlight_cpp":"b6e4fc476a4a912e7612","react-syntax-highlighter_languages_highlight_crmsh":"a5e4d5ba17f3419c4f69","react-syntax-highlighter_languages_highlight_crystal":"d1d9d35393c218753620","react-syntax-highlighter_languages_highlight_csharp":"fddfd1dfe9f1ef1ea792","react-syntax-highlighter_languages_highlight_csp":"8056e7f0ef6a8c2bc472","react-syntax-highlighter_languages_highlight_css":"99c9f0c3c4e6584608f9","react-syntax-highlighter_languages_highlight_d":"7cb3d917d44d5415c1ef","react-syntax-highlighter_languages_highlight_dart":"62eb094a061b55eb46a5","react-syntax-highlighter_languages_highlight_delphi":"d344bf4978a1a2cea3a3","react-syntax-highlighter_languages_highlight_diff":"c5831f348a3bbcdee105","react-syntax-highlighter_languages_highlight_django":"64f67eb6718a1ca43c44","react-syntax-highlighter_languages_highlight_dns":"75054cb9344e1fbcb1b4","react-syntax-highlighter_languages_highlight_dockerfile":"0c3f132879cca009602b","react-syntax-highlighter_languages_highlight_dos":"4c7ea20d9e01bd2d8d52","react-syntax-highlighter_languages_highlight_dsconfig":"b28587872552246de43b","react-syntax-highlighter_languages_highlight_dts":"94d502261e9d63c5c01f","react-syntax-highlighter_languages_highlight_dust":"bc1a6d463268ce2538d0","react-syntax-highlighter_languages_highlight_ebnf":"317019ec3c7ae7b903fc","react-syntax-highlighter_languages_highlight_elixir":"64de0395c03d85cfac55","react-syntax-highlighter_languages_highlight_elm":"0b418cde6638ed6d9ff4","react-syntax-highlighter_languages_highlight_erb":"572822dbcbf698655415","react-syntax-highlighter_languages_highlight_erlangRepl":"21d0abfeac9bd7851496","react-syntax-highlighter_languages_highlight_erlang":"7e6546c99a36d7b220b2","react-syntax-highlighter_languages_highlight_excel":"ae404756b84089945ec3","react-syntax-highlighter_languages_highlight_fix":"380287cbb447ef0f408e","react-syntax-highlighter_languages_highlight_flix":"0374ffb6c386fac5c828","react-syntax-highlighter_languages_highlight_fortran":"c857cfc62bf5bdda6e91","react-syntax-highlighter_languages_highlight_fsharp":"d83316c2efeaa42e6b19","react-syntax-highlighter_languages_highlight_gams":"3f51fdb6a0c6a1dc90f3","react-syntax-highlighter_languages_highlight_gauss":"19e1b3dc27fcbf2b8be3","react-syntax-highlighter_languages_highlight_gcode":"da63b42b83cb7902f553","react-syntax-highlighter_languages_highlight_gherkin":"4e40bdeeaba631059560","react-syntax-highlighter_languages_highlight_glsl":"2d88b99d48129b660ec3","react-syntax-highlighter_languages_highlight_gml":"8b6549f829c00d61682d","react-syntax-highlighter_languages_highlight_go":"3cb1247e9bfd05e88b59","react-syntax-highlighter_languages_highlight_golo":"56e27192fe003526dff3","react-syntax-highlighter_languages_highlight_gradle":"6f18393c50c6ee6545af","react-syntax-highlighter_languages_highlight_groovy":"c537f83a9d3087bb463a","react-syntax-highlighter_languages_highlight_haml":"dfcf22dc43b4a2f189ba","react-syntax-highlighter_languages_highlight_handlebars":"1ceb6ed5c4ddf8886177","react-syntax-highlighter_languages_highlight_haskell":"a669ff7b6d435c93ab64","react-syntax-highlighter_languages_highlight_haxe":"7ff554044db435e6b2a6","react-syntax-highlighter_languages_highlight_hsp":"f00dd5294696442d671c","react-syntax-highlighter_languages_highlight_htmlbars":"525763c161899ede0514","react-syntax-highlighter_languages_highlight_http":"87dee2d58366904a0e37","react-syntax-highlighter_languages_highlight_hy":"463406bb82b8dab1a553","react-syntax-highlighter_languages_highlight_inform7":"2700ea83837030341800","react-syntax-highlighter_languages_highlight_ini":"e4c0e1db482f607221d0","react-syntax-highlighter_languages_highlight_irpf90":"2f0795879bbc23403d0a","react-syntax-highlighter_languages_highlight_isbl":"3b46897687fe750608ef","react-syntax-highlighter_languages_highlight_java":"a6cb174725d3545d5601","react-syntax-highlighter_languages_highlight_javascript":"94b38770a1d4c9bf358d","react-syntax-highlighter_languages_highlight_jbossCli":"c3951d00ec4f0690f737","react-syntax-highlighter_languages_highlight_json":"760eff5b1f335a1bfb63","react-syntax-highlighter_languages_highlight_juliaRepl":"6b89dab3afa974d600ac","react-syntax-highlighter_languages_highlight_julia":"92dc94c76f719cbbd733","react-syntax-highlighter_languages_highlight_kotlin":"d9ae9457b8b91cca3a06","react-syntax-highlighter_languages_highlight_lasso":"392224c5cfdc87002d67","react-syntax-highlighter_languages_highlight_latex":"d7afef6f7e38d4448c77","react-syntax-highlighter_languages_highlight_ldif":"2b2dee05ad5cf148122e","react-syntax-highlighter_languages_highlight_leaf":"c4416987f06a7a63ea4a","react-syntax-highlighter_languages_highlight_less":"544cc575ddd8f05d8871","react-syntax-highlighter_languages_highlight_lisp":"26a7124f4695e530d2ea","react-syntax-highlighter_languages_highlight_livecodeserver":"432d5119c66fa54cf0c0","react-syntax-highlighter_languages_highlight_livescript":"3b3861b155a2bda9c09c","react-syntax-highlighter_languages_highlight_llvm":"980e24f96d011a45c8e5","react-syntax-highlighter_languages_highlight_lsl":"b74d8170a11b2fdca32b","react-syntax-highlighter_languages_highlight_lua":"25faa2f69b4e39fbd087","react-syntax-highlighter_languages_highlight_makefile":"1be98466e96520d3ae21","react-syntax-highlighter_languages_highlight_markdown":"1ab464cc7543c2cb0a95","react-syntax-highlighter_languages_highlight_mathematica":"c0b2168e4091f78b3b94","react-syntax-highlighter_languages_highlight_matlab":"3c40b6ad0ec019242bfd","react-syntax-highlighter_languages_highlight_maxima":"e56398d1b492a8509ab2","react-syntax-highlighter_languages_highlight_mel":"d606e5ee0e57595bc628","react-syntax-highlighter_languages_highlight_mercury":"1a3a5e23ac61959077fa","react-syntax-highlighter_languages_highlight_mipsasm":"6ca467a8ca4cdd6d81b0","react-syntax-highlighter_languages_highlight_mizar":"8bc75fdf699e6568f8bd","react-syntax-highlighter_languages_highlight_mojolicious":"bfe67d8c69a352ba23a9","react-syntax-highlighter_languages_highlight_monkey":"1a7da6623bc83566aea4","react-syntax-highlighter_languages_highlight_moonscript":"5c5660d4c6c3a8f11f87","react-syntax-highlighter_languages_highlight_n1ql":"171834eb75efb5d52d38","react-syntax-highlighter_languages_highlight_nginx":"f363f18888b395af0851","react-syntax-highlighter_languages_highlight_nim":"03d7ea0895a9b7e5185c","react-syntax-highlighter_languages_highlight_nix":"4f045294def27f4c8a00","react-syntax-highlighter_languages_highlight_nodeRepl":"84d57d4b36dccd7bc245","react-syntax-highlighter_languages_highlight_nsis":"9763a9fcdb69ee118e28","react-syntax-highlighter_languages_highlight_objectivec":"4e75686750e8d560673b","react-syntax-highlighter_languages_highlight_ocaml":"fb06ed4c871a9064eb15","react-syntax-highlighter_languages_highlight_openscad":"e98a3bc310dccd91af1a","react-syntax-highlighter_languages_highlight_oxygene":"8fe96bee15b2b3989072","react-syntax-highlighter_languages_highlight_parser3":"f79889418b2d727e3456","react-syntax-highlighter_languages_highlight_perl":"0fef13743ec20d0cc613","react-syntax-highlighter_languages_highlight_pf":"686833f1fdb4b80ba199","react-syntax-highlighter_languages_highlight_pgsql":"b70354727065ebe0d134","react-syntax-highlighter_languages_highlight_phpTemplate":"f2f893a6f2e60b5a64cd","react-syntax-highlighter_languages_highlight_php":"4e0b02f9a5b63355461f","react-syntax-highlighter_languages_highlight_plaintext":"1b5be74598188eb2e327","react-syntax-highlighter_languages_highlight_pony":"4587b1eb4d51edf26749","react-syntax-highlighter_languages_highlight_powershell":"fb145c361016d16fb1b6","react-syntax-highlighter_languages_highlight_processing":"94adf18a87548afac263","react-syntax-highlighter_languages_highlight_profile":"1ae133402f20977c67d6","react-syntax-highlighter_languages_highlight_prolog":"c6966cb40b380b155bf9","react-syntax-highlighter_languages_highlight_properties":"9659900bbcc94ae8b894","react-syntax-highlighter_languages_highlight_protobuf":"fd906723040ff4be16a1","react-syntax-highlighter_languages_highlight_puppet":"846472b449ba77bbd315","react-syntax-highlighter_languages_highlight_purebasic":"1d2375212d9436bbc49e","react-syntax-highlighter_languages_highlight_pythonRepl":"e4a736619526215ad9ce","react-syntax-highlighter_languages_highlight_python":"816f204d4afc2144bdf4","react-syntax-highlighter_languages_highlight_q":"5c004c8ce88682eb91a8","react-syntax-highlighter_languages_highlight_qml":"3b0010e47be05a8c80a3","react-syntax-highlighter_languages_highlight_r":"cd785247ada904bd23d5","react-syntax-highlighter_languages_highlight_reasonml":"0c98bd09ab0e3241ed16","react-syntax-highlighter_languages_highlight_rib":"cc8488bc23091c292e13","react-syntax-highlighter_languages_highlight_roboconf":"ab67d174986f11b099af","react-syntax-highlighter_languages_highlight_routeros":"585831c1e183d903cb37","react-syntax-highlighter_languages_highlight_rsl":"b2228e34f2080e68bec3","react-syntax-highlighter_languages_highlight_ruby":"1f79707ab7b009762460","react-syntax-highlighter_languages_highlight_ruleslanguage":"49ee95d2b8f464dd6bc5","react-syntax-highlighter_languages_highlight_rust":"77ef77fc36da2558d04d","react-syntax-highlighter_languages_highlight_sas":"2386376c8b48ab485a43","react-syntax-highlighter_languages_highlight_scala":"3ea06168e140cff267fa","react-syntax-highlighter_languages_highlight_scheme":"20bcd86b1c996d080773","react-syntax-highlighter_languages_highlight_scilab":"030e5a81a3dea0fffa5d","react-syntax-highlighter_languages_highlight_scss":"90da3ab3451e70f9f537","react-syntax-highlighter_languages_highlight_shell":"92bf89f834c0c25aa067","react-syntax-highlighter_languages_highlight_smali":"ea9dadecbf4fcaef16d2","react-syntax-highlighter_languages_highlight_smalltalk":"93b94e5229d8159a5137","react-syntax-highlighter_languages_highlight_sml":"bf3c13232bb6642b17d0","react-syntax-highlighter_languages_highlight_sqf":"a1830f6e3e97ccf31e58","react-syntax-highlighter_languages_highlight_sql":"dbaae537422d0493d197","react-syntax-highlighter_languages_highlight_sqlMore":"060267692ec62386b2c6","react-syntax-highlighter_languages_highlight_stan":"5f27d2ef3397ed5ec157","react-syntax-highlighter_languages_highlight_stata":"78078eacff28687165ee","react-syntax-highlighter_languages_highlight_step21":"a511b112183e0f29fdff","react-syntax-highlighter_languages_highlight_stylus":"0f27b6e1434a52fd56f2","react-syntax-highlighter_languages_highlight_subunit":"3203c21663f7237fca8e","react-syntax-highlighter_languages_highlight_swift":"6b540427593845456831","react-syntax-highlighter_languages_highlight_taggerscript":"7e9e0d5645931bb8728f","react-syntax-highlighter_languages_highlight_tap":"38b57d50d1366d3abdf5","react-syntax-highlighter_languages_highlight_tcl":"6a1964b455cbd3c746b3","react-syntax-highlighter_languages_highlight_thrift":"d9599439b61fab1a4dbe","react-syntax-highlighter_languages_highlight_tp":"8f0579fe84cf0da62c63","react-syntax-highlighter_languages_highlight_twig":"adb05664d8ead9c0f4f5","react-syntax-highlighter_languages_highlight_typescript":"5305a523f29eb2fb304c","react-syntax-highlighter_languages_highlight_vala":"3962e8149a61cb36c72b","react-syntax-highlighter_languages_highlight_vbnet":"7e4a145cb3ec6f5308f6","react-syntax-highlighter_languages_highlight_vbscriptHtml":"0c9024c8e60254dc74b1","react-syntax-highlighter_languages_highlight_vbscript":"a9dc58a3ff0bef5132b1","react-syntax-highlighter_languages_highlight_verilog":"37f150c1b2eba36dadc8","react-syntax-highlighter_languages_highlight_vhdl":"0736ae409e90a23c7fcc","react-syntax-highlighter_languages_highlight_vim":"0d7fcafad620d521f5c0","react-syntax-highlighter_languages_highlight_x86asm":"af6357643ca2d4a7a004","react-syntax-highlighter_languages_highlight_xl":"517ec9c47fdf9e1b6da6","react-syntax-highlighter_languages_highlight_xml":"518277ca90415b345f82","react-syntax-highlighter_languages_highlight_xquery":"90e82179f18cfff9fbb6","react-syntax-highlighter_languages_highlight_yaml":"4c30554e8274467dd9f3","react-syntax-highlighter_languages_highlight_zephir":"1643dd9c561dcd3de928"}[chunkId] + ".js";
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/global */
/******/ 	(() => {
/******/ 		__webpack_require__.g = (function() {
/******/ 			if (typeof globalThis === 'object') return globalThis;
/******/ 			try {
/******/ 				return this || new Function('return this')();
/******/ 			} catch (e) {
/******/ 				if (typeof window === 'object') return window;
/******/ 			}
/******/ 		})();
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/load script */
/******/ 	(() => {
/******/ 		var inProgress = {};
/******/ 		var dataWebpackPrefix = "papyri-lab:";
/******/ 		// loadScript function to load a script via script tag
/******/ 		__webpack_require__.l = (url, done, key, chunkId) => {
/******/ 			if(inProgress[url]) { inProgress[url].push(done); return; }
/******/ 			var script, needAttach;
/******/ 			if(key !== undefined) {
/******/ 				var scripts = document.getElementsByTagName("script");
/******/ 				for(var i = 0; i < scripts.length; i++) {
/******/ 					var s = scripts[i];
/******/ 					if(s.getAttribute("src") == url || s.getAttribute("data-webpack") == dataWebpackPrefix + key) { script = s; break; }
/******/ 				}
/******/ 			}
/******/ 			if(!script) {
/******/ 				needAttach = true;
/******/ 				script = document.createElement('script');
/******/ 		
/******/ 				script.charset = 'utf-8';
/******/ 				script.timeout = 120;
/******/ 				if (__webpack_require__.nc) {
/******/ 					script.setAttribute("nonce", __webpack_require__.nc);
/******/ 				}
/******/ 				script.setAttribute("data-webpack", dataWebpackPrefix + key);
/******/ 		
/******/ 				script.src = url;
/******/ 			}
/******/ 			inProgress[url] = [done];
/******/ 			var onScriptComplete = (prev, event) => {
/******/ 				// avoid mem leaks in IE.
/******/ 				script.onerror = script.onload = null;
/******/ 				clearTimeout(timeout);
/******/ 				var doneFns = inProgress[url];
/******/ 				delete inProgress[url];
/******/ 				script.parentNode && script.parentNode.removeChild(script);
/******/ 				doneFns && doneFns.forEach((fn) => (fn(event)));
/******/ 				if(prev) return prev(event);
/******/ 			}
/******/ 			var timeout = setTimeout(onScriptComplete.bind(null, undefined, { type: 'timeout', target: script }), 120000);
/******/ 			script.onerror = onScriptComplete.bind(null, script.onerror);
/******/ 			script.onload = onScriptComplete.bind(null, script.onload);
/******/ 			needAttach && document.head.appendChild(script);
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/sharing */
/******/ 	(() => {
/******/ 		__webpack_require__.S = {};
/******/ 		var initPromises = {};
/******/ 		var initTokens = {};
/******/ 		__webpack_require__.I = (name, initScope) => {
/******/ 			if(!initScope) initScope = [];
/******/ 			// handling circular init calls
/******/ 			var initToken = initTokens[name];
/******/ 			if(!initToken) initToken = initTokens[name] = {};
/******/ 			if(initScope.indexOf(initToken) >= 0) return;
/******/ 			initScope.push(initToken);
/******/ 			// only runs once
/******/ 			if(initPromises[name]) return initPromises[name];
/******/ 			// creates a new share scope if needed
/******/ 			if(!__webpack_require__.o(__webpack_require__.S, name)) __webpack_require__.S[name] = {};
/******/ 			// runs all init snippets from all modules reachable
/******/ 			var scope = __webpack_require__.S[name];
/******/ 			var warn = (msg) => {
/******/ 				if (typeof console !== "undefined" && console.warn) console.warn(msg);
/******/ 			};
/******/ 			var uniqueName = "papyri-lab";
/******/ 			var register = (name, version, factory, eager) => {
/******/ 				var versions = scope[name] = scope[name] || {};
/******/ 				var activeVersion = versions[version];
/******/ 				if(!activeVersion || (!activeVersion.loaded && (!eager != !activeVersion.eager ? eager : uniqueName > activeVersion.from))) versions[version] = { get: factory, from: uniqueName, eager: !!eager };
/******/ 			};
/******/ 			var initExternal = (id) => {
/******/ 				var handleError = (err) => (warn("Initialization of sharing external failed: " + err));
/******/ 				try {
/******/ 					var module = __webpack_require__(id);
/******/ 					if(!module) return;
/******/ 					var initFn = (module) => (module && module.init && module.init(__webpack_require__.S[name], initScope))
/******/ 					if(module.then) return promises.push(module.then(initFn, handleError));
/******/ 					var initResult = initFn(module);
/******/ 					if(initResult && initResult.then) return promises.push(initResult['catch'](handleError));
/******/ 				} catch(err) { handleError(err); }
/******/ 			}
/******/ 			var promises = [];
/******/ 			switch(name) {
/******/ 				case "default": {
/******/ 					register("myst-to-react", "0.5.20", () => (Promise.all([__webpack_require__.e("vendors-node_modules_myst-to-react_dist_index_js"), __webpack_require__.e("vendors-node_modules_myst-theme_providers_dist_index_js"), __webpack_require__.e("webpack_sharing_consume_default_react"), __webpack_require__.e("webpack_sharing_consume_default_react-dom")]).then(() => (() => (__webpack_require__(/*! ./node_modules/myst-to-react/dist/index.js */ "./node_modules/myst-to-react/dist/index.js"))))));
/******/ 					register("papyri-lab", "0.1.0", () => (Promise.all([__webpack_require__.e("vendors-node_modules_myst-theme_providers_dist_index_js"), __webpack_require__.e("webpack_sharing_consume_default_react"), __webpack_require__.e("lib_index_js")]).then(() => (() => (__webpack_require__(/*! ./lib/index.js */ "./lib/index.js"))))));
/******/ 				}
/******/ 				break;
/******/ 			}
/******/ 			if(!promises.length) return initPromises[name] = 1;
/******/ 			return initPromises[name] = Promise.all(promises).then(() => (initPromises[name] = 1));
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/publicPath */
/******/ 	(() => {
/******/ 		var scriptUrl;
/******/ 		if (__webpack_require__.g.importScripts) scriptUrl = __webpack_require__.g.location + "";
/******/ 		var document = __webpack_require__.g.document;
/******/ 		if (!scriptUrl && document) {
/******/ 			if (document.currentScript)
/******/ 				scriptUrl = document.currentScript.src;
/******/ 			if (!scriptUrl) {
/******/ 				var scripts = document.getElementsByTagName("script");
/******/ 				if(scripts.length) {
/******/ 					var i = scripts.length - 1;
/******/ 					while (i > -1 && !scriptUrl) scriptUrl = scripts[i--].src;
/******/ 				}
/******/ 			}
/******/ 		}
/******/ 		// When supporting browsers where an automatic publicPath is not supported you must specify an output.publicPath manually via configuration
/******/ 		// or pass an empty string ("") and set the __webpack_public_path__ variable from your code to use your own logic.
/******/ 		if (!scriptUrl) throw new Error("Automatic publicPath is not supported in this browser");
/******/ 		scriptUrl = scriptUrl.replace(/#.*$/, "").replace(/\?.*$/, "").replace(/\/[^\/]+$/, "/");
/******/ 		__webpack_require__.p = scriptUrl;
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/consumes */
/******/ 	(() => {
/******/ 		var parseVersion = (str) => {
/******/ 			// see webpack/lib/util/semver.js for original code
/******/ 			var p=p=>{return p.split(".").map((p=>{return+p==p?+p:p}))},n=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(str),r=n[1]?p(n[1]):[];return n[2]&&(r.length++,r.push.apply(r,p(n[2]))),n[3]&&(r.push([]),r.push.apply(r,p(n[3]))),r;
/******/ 		}
/******/ 		var versionLt = (a, b) => {
/******/ 			// see webpack/lib/util/semver.js for original code
/******/ 			a=parseVersion(a),b=parseVersion(b);for(var r=0;;){if(r>=a.length)return r<b.length&&"u"!=(typeof b[r])[0];var e=a[r],n=(typeof e)[0];if(r>=b.length)return"u"==n;var t=b[r],f=(typeof t)[0];if(n!=f)return"o"==n&&"n"==f||("s"==f||"u"==n);if("o"!=n&&"u"!=n&&e!=t)return e<t;r++}
/******/ 		}
/******/ 		var rangeToString = (range) => {
/******/ 			// see webpack/lib/util/semver.js for original code
/******/ 			var r=range[0],n="";if(1===range.length)return"*";if(r+.5){n+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var e=1,a=1;a<range.length;a++){e--,n+="u"==(typeof(t=range[a]))[0]?"-":(e>0?".":"")+(e=2,t)}return n}var g=[];for(a=1;a<range.length;a++){var t=range[a];g.push(0===t?"not("+o()+")":1===t?"("+o()+" || "+o()+")":2===t?g.pop()+" "+g.pop():rangeToString(t))}return o();function o(){return g.pop().replace(/^\((.+)\)$/,"$1")}
/******/ 		}
/******/ 		var satisfy = (range, version) => {
/******/ 			// see webpack/lib/util/semver.js for original code
/******/ 			if(0 in range){version=parseVersion(version);var e=range[0],r=e<0;r&&(e=-e-1);for(var n=0,i=1,a=!0;;i++,n++){var f,s,g=i<range.length?(typeof range[i])[0]:"";if(n>=version.length||"o"==(s=(typeof(f=version[n]))[0]))return!a||("u"==g?i>e&&!r:""==g!=r);if("u"==s){if(!a||"u"!=g)return!1}else if(a)if(g==s)if(i<=e){if(f!=range[i])return!1}else{if(r?f>range[i]:f<range[i])return!1;f!=range[i]&&(a=!1)}else if("s"!=g&&"n"!=g){if(r||i<=e)return!1;a=!1,i--}else{if(i<=e||s<g!=r)return!1;a=!1}else"s"!=g&&"n"!=g&&(a=!1,i--)}}var t=[],o=t.pop.bind(t);for(n=1;n<range.length;n++){var u=range[n];t.push(1==u?o()|o():2==u?o()&o():u?satisfy(u,version):!o())}return!!o();
/******/ 		}
/******/ 		var ensureExistence = (scopeName, key) => {
/******/ 			var scope = __webpack_require__.S[scopeName];
/******/ 			if(!scope || !__webpack_require__.o(scope, key)) throw new Error("Shared module " + key + " doesn't exist in shared scope " + scopeName);
/******/ 			return scope;
/******/ 		};
/******/ 		var findVersion = (scope, key) => {
/******/ 			var versions = scope[key];
/******/ 			var key = Object.keys(versions).reduce((a, b) => {
/******/ 				return !a || versionLt(a, b) ? b : a;
/******/ 			}, 0);
/******/ 			return key && versions[key]
/******/ 		};
/******/ 		var findSingletonVersionKey = (scope, key) => {
/******/ 			var versions = scope[key];
/******/ 			return Object.keys(versions).reduce((a, b) => {
/******/ 				return !a || (!versions[a].loaded && versionLt(a, b)) ? b : a;
/******/ 			}, 0);
/******/ 		};
/******/ 		var getInvalidSingletonVersionMessage = (scope, key, version, requiredVersion) => {
/******/ 			return "Unsatisfied version " + version + " from " + (version && scope[key][version].from) + " of shared singleton module " + key + " (required " + rangeToString(requiredVersion) + ")"
/******/ 		};
/******/ 		var getSingleton = (scope, scopeName, key, requiredVersion) => {
/******/ 			var version = findSingletonVersionKey(scope, key);
/******/ 			return get(scope[key][version]);
/******/ 		};
/******/ 		var getSingletonVersion = (scope, scopeName, key, requiredVersion) => {
/******/ 			var version = findSingletonVersionKey(scope, key);
/******/ 			if (!satisfy(requiredVersion, version)) warn(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));
/******/ 			return get(scope[key][version]);
/******/ 		};
/******/ 		var getStrictSingletonVersion = (scope, scopeName, key, requiredVersion) => {
/******/ 			var version = findSingletonVersionKey(scope, key);
/******/ 			if (!satisfy(requiredVersion, version)) throw new Error(getInvalidSingletonVersionMessage(scope, key, version, requiredVersion));
/******/ 			return get(scope[key][version]);
/******/ 		};
/******/ 		var findValidVersion = (scope, key, requiredVersion) => {
/******/ 			var versions = scope[key];
/******/ 			var key = Object.keys(versions).reduce((a, b) => {
/******/ 				if (!satisfy(requiredVersion, b)) return a;
/******/ 				return !a || versionLt(a, b) ? b : a;
/******/ 			}, 0);
/******/ 			return key && versions[key]
/******/ 		};
/******/ 		var getInvalidVersionMessage = (scope, scopeName, key, requiredVersion) => {
/******/ 			var versions = scope[key];
/******/ 			return "No satisfying version (" + rangeToString(requiredVersion) + ") of shared module " + key + " found in shared scope " + scopeName + ".\n" +
/******/ 				"Available versions: " + Object.keys(versions).map((key) => {
/******/ 				return key + " from " + versions[key].from;
/******/ 			}).join(", ");
/******/ 		};
/******/ 		var getValidVersion = (scope, scopeName, key, requiredVersion) => {
/******/ 			var entry = findValidVersion(scope, key, requiredVersion);
/******/ 			if(entry) return get(entry);
/******/ 			throw new Error(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));
/******/ 		};
/******/ 		var warn = (msg) => {
/******/ 			if (typeof console !== "undefined" && console.warn) console.warn(msg);
/******/ 		};
/******/ 		var warnInvalidVersion = (scope, scopeName, key, requiredVersion) => {
/******/ 			warn(getInvalidVersionMessage(scope, scopeName, key, requiredVersion));
/******/ 		};
/******/ 		var get = (entry) => {
/******/ 			entry.loaded = 1;
/******/ 			return entry.get()
/******/ 		};
/******/ 		var init = (fn) => (function(scopeName, a, b, c) {
/******/ 			var promise = __webpack_require__.I(scopeName);
/******/ 			if (promise && promise.then) return promise.then(fn.bind(fn, scopeName, __webpack_require__.S[scopeName], a, b, c));
/******/ 			return fn(scopeName, __webpack_require__.S[scopeName], a, b, c);
/******/ 		});
/******/ 		
/******/ 		var load = /*#__PURE__*/ init((scopeName, scope, key) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return get(findVersion(scope, key));
/******/ 		});
/******/ 		var loadFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {
/******/ 			return scope && __webpack_require__.o(scope, key) ? get(findVersion(scope, key)) : fallback();
/******/ 		});
/******/ 		var loadVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));
/******/ 		});
/******/ 		var loadSingleton = /*#__PURE__*/ init((scopeName, scope, key) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return getSingleton(scope, scopeName, key);
/******/ 		});
/******/ 		var loadSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return getSingletonVersion(scope, scopeName, key, version);
/******/ 		});
/******/ 		var loadStrictVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return getValidVersion(scope, scopeName, key, version);
/******/ 		});
/******/ 		var loadStrictSingletonVersionCheck = /*#__PURE__*/ init((scopeName, scope, key, version) => {
/******/ 			ensureExistence(scopeName, key);
/******/ 			return getStrictSingletonVersion(scope, scopeName, key, version);
/******/ 		});
/******/ 		var loadVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {
/******/ 			if(!scope || !__webpack_require__.o(scope, key)) return fallback();
/******/ 			return get(findValidVersion(scope, key, version) || warnInvalidVersion(scope, scopeName, key, version) || findVersion(scope, key));
/******/ 		});
/******/ 		var loadSingletonFallback = /*#__PURE__*/ init((scopeName, scope, key, fallback) => {
/******/ 			if(!scope || !__webpack_require__.o(scope, key)) return fallback();
/******/ 			return getSingleton(scope, scopeName, key);
/******/ 		});
/******/ 		var loadSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {
/******/ 			if(!scope || !__webpack_require__.o(scope, key)) return fallback();
/******/ 			return getSingletonVersion(scope, scopeName, key, version);
/******/ 		});
/******/ 		var loadStrictVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {
/******/ 			var entry = scope && __webpack_require__.o(scope, key) && findValidVersion(scope, key, version);
/******/ 			return entry ? get(entry) : fallback();
/******/ 		});
/******/ 		var loadStrictSingletonVersionCheckFallback = /*#__PURE__*/ init((scopeName, scope, key, version, fallback) => {
/******/ 			if(!scope || !__webpack_require__.o(scope, key)) return fallback();
/******/ 			return getStrictSingletonVersion(scope, scopeName, key, version);
/******/ 		});
/******/ 		var installedModules = {};
/******/ 		var moduleToHandlerMapping = {
/******/ 			"webpack/sharing/consume/default/react": () => (loadSingletonVersionCheck("default", "react", [1,18,2,0])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/application": () => (loadSingletonVersionCheck("default", "@jupyterlab/application", [1,4,0,9])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/apputils": () => (loadSingletonVersionCheck("default", "@jupyterlab/apputils", [1,4,1,9])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/notebook": () => (loadSingletonVersionCheck("default", "@jupyterlab/notebook", [1,4,0,9])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/settingregistry": () => (loadSingletonVersionCheck("default", "@jupyterlab/settingregistry", [1,4,0,9])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/coreutils": () => (loadSingletonVersionCheck("default", "@jupyterlab/coreutils", [1,6,0,9])),
/******/ 			"webpack/sharing/consume/default/@jupyterlab/services": () => (loadSingletonVersionCheck("default", "@jupyterlab/services", [1,7,0,9])),
/******/ 			"webpack/sharing/consume/default/myst-to-react/myst-to-react": () => (loadStrictVersionCheckFallback("default", "myst-to-react", [2,0,5,20], () => (Promise.all([__webpack_require__.e("vendors-node_modules_myst-to-react_dist_index_js"), __webpack_require__.e("webpack_sharing_consume_default_react-dom")]).then(() => (() => (__webpack_require__(/*! myst-to-react */ "./node_modules/myst-to-react/dist/index.js"))))))),
/******/ 			"webpack/sharing/consume/default/@lumino/signaling": () => (loadSingletonVersionCheck("default", "@lumino/signaling", [1,2,0,0])),
/******/ 			"webpack/sharing/consume/default/react-dom": () => (loadSingletonVersionCheck("default", "react-dom", [1,18,2,0]))
/******/ 		};
/******/ 		// no consumes in initial chunks
/******/ 		var chunkMapping = {
/******/ 			"webpack_sharing_consume_default_react": [
/******/ 				"webpack/sharing/consume/default/react"
/******/ 			],
/******/ 			"lib_index_js": [
/******/ 				"webpack/sharing/consume/default/@jupyterlab/application",
/******/ 				"webpack/sharing/consume/default/@jupyterlab/apputils",
/******/ 				"webpack/sharing/consume/default/@jupyterlab/notebook",
/******/ 				"webpack/sharing/consume/default/@jupyterlab/settingregistry",
/******/ 				"webpack/sharing/consume/default/@jupyterlab/coreutils",
/******/ 				"webpack/sharing/consume/default/@jupyterlab/services",
/******/ 				"webpack/sharing/consume/default/myst-to-react/myst-to-react",
/******/ 				"webpack/sharing/consume/default/@lumino/signaling"
/******/ 			],
/******/ 			"webpack_sharing_consume_default_react-dom": [
/******/ 				"webpack/sharing/consume/default/react-dom"
/******/ 			]
/******/ 		};
/******/ 		__webpack_require__.f.consumes = (chunkId, promises) => {
/******/ 			if(__webpack_require__.o(chunkMapping, chunkId)) {
/******/ 				chunkMapping[chunkId].forEach((id) => {
/******/ 					if(__webpack_require__.o(installedModules, id)) return promises.push(installedModules[id]);
/******/ 					var onFactory = (factory) => {
/******/ 						installedModules[id] = 0;
/******/ 						__webpack_require__.m[id] = (module) => {
/******/ 							delete __webpack_require__.c[id];
/******/ 							module.exports = factory();
/******/ 						}
/******/ 					};
/******/ 					var onError = (error) => {
/******/ 						delete installedModules[id];
/******/ 						__webpack_require__.m[id] = (module) => {
/******/ 							delete __webpack_require__.c[id];
/******/ 							throw error;
/******/ 						}
/******/ 					};
/******/ 					try {
/******/ 						var promise = moduleToHandlerMapping[id]();
/******/ 						if(promise.then) {
/******/ 							promises.push(installedModules[id] = promise.then(onFactory)['catch'](onError));
/******/ 						} else onFactory(promise);
/******/ 					} catch(e) { onError(e); }
/******/ 				});
/******/ 			}
/******/ 		}
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/jsonp chunk loading */
/******/ 	(() => {
/******/ 		// no baseURI
/******/ 		
/******/ 		// object to store loaded and loading chunks
/******/ 		// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 		// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
/******/ 		var installedChunks = {
/******/ 			"papyri-lab": 0
/******/ 		};
/******/ 		
/******/ 		__webpack_require__.f.j = (chunkId, promises) => {
/******/ 				// JSONP chunk loading for javascript
/******/ 				var installedChunkData = __webpack_require__.o(installedChunks, chunkId) ? installedChunks[chunkId] : undefined;
/******/ 				if(installedChunkData !== 0) { // 0 means "already installed".
/******/ 		
/******/ 					// a Promise means "currently loading".
/******/ 					if(installedChunkData) {
/******/ 						promises.push(installedChunkData[2]);
/******/ 					} else {
/******/ 						if(!/^webpack_sharing_consume_default_react(|\-dom)$/.test(chunkId)) {
/******/ 							// setup Promise in chunk cache
/******/ 							var promise = new Promise((resolve, reject) => (installedChunkData = installedChunks[chunkId] = [resolve, reject]));
/******/ 							promises.push(installedChunkData[2] = promise);
/******/ 		
/******/ 							// start chunk loading
/******/ 							var url = __webpack_require__.p + __webpack_require__.u(chunkId);
/******/ 							// create error before stack unwound to get useful stacktrace later
/******/ 							var error = new Error();
/******/ 							var loadingEnded = (event) => {
/******/ 								if(__webpack_require__.o(installedChunks, chunkId)) {
/******/ 									installedChunkData = installedChunks[chunkId];
/******/ 									if(installedChunkData !== 0) installedChunks[chunkId] = undefined;
/******/ 									if(installedChunkData) {
/******/ 										var errorType = event && (event.type === 'load' ? 'missing' : event.type);
/******/ 										var realSrc = event && event.target && event.target.src;
/******/ 										error.message = 'Loading chunk ' + chunkId + ' failed.\n(' + errorType + ': ' + realSrc + ')';
/******/ 										error.name = 'ChunkLoadError';
/******/ 										error.type = errorType;
/******/ 										error.request = realSrc;
/******/ 										installedChunkData[1](error);
/******/ 									}
/******/ 								}
/******/ 							};
/******/ 							__webpack_require__.l(url, loadingEnded, "chunk-" + chunkId, chunkId);
/******/ 						} else installedChunks[chunkId] = 0;
/******/ 					}
/******/ 				}
/******/ 		};
/******/ 		
/******/ 		// no prefetching
/******/ 		
/******/ 		// no preloaded
/******/ 		
/******/ 		// no HMR
/******/ 		
/******/ 		// no HMR manifest
/******/ 		
/******/ 		// no on chunks loaded
/******/ 		
/******/ 		// install a JSONP callback for chunk loading
/******/ 		var webpackJsonpCallback = (parentChunkLoadingFunction, data) => {
/******/ 			var [chunkIds, moreModules, runtime] = data;
/******/ 			// add "moreModules" to the modules object,
/******/ 			// then flag all "chunkIds" as loaded and fire callback
/******/ 			var moduleId, chunkId, i = 0;
/******/ 			if(chunkIds.some((id) => (installedChunks[id] !== 0))) {
/******/ 				for(moduleId in moreModules) {
/******/ 					if(__webpack_require__.o(moreModules, moduleId)) {
/******/ 						__webpack_require__.m[moduleId] = moreModules[moduleId];
/******/ 					}
/******/ 				}
/******/ 				if(runtime) var result = runtime(__webpack_require__);
/******/ 			}
/******/ 			if(parentChunkLoadingFunction) parentChunkLoadingFunction(data);
/******/ 			for(;i < chunkIds.length; i++) {
/******/ 				chunkId = chunkIds[i];
/******/ 				if(__webpack_require__.o(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 					installedChunks[chunkId][0]();
/******/ 				}
/******/ 				installedChunks[chunkId] = 0;
/******/ 			}
/******/ 		
/******/ 		}
/******/ 		
/******/ 		var chunkLoadingGlobal = self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || [];
/******/ 		chunkLoadingGlobal.forEach(webpackJsonpCallback.bind(null, 0));
/******/ 		chunkLoadingGlobal.push = webpackJsonpCallback.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/nonce */
/******/ 	(() => {
/******/ 		__webpack_require__.nc = undefined;
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// module cache are used so entry inlining is disabled
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	var __webpack_exports__ = __webpack_require__("webpack/container/entry/papyri-lab");
/******/ 	(_JUPYTERLAB = typeof _JUPYTERLAB === "undefined" ? {} : _JUPYTERLAB)["papyri-lab"] = __webpack_exports__;
/******/ 	
/******/ })()
;
//# sourceMappingURL=remoteEntry.12ed553f2de11eba4b62.js.map