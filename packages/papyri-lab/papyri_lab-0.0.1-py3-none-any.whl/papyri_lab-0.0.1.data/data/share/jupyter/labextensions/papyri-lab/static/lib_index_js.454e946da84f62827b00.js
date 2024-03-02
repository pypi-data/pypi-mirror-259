"use strict";
(self["webpackChunkpapyri_lab"] = self["webpackChunkpapyri_lab"] || []).push([["lib_index_js"],{

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   requestAPI: () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'papyri-lab', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _kernelspy__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./kernelspy */ "./lib/kernelspy.js");
/* harmony import */ var _widgets__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgets */ "./lib/widgets.js");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
// Entry point for the Papyri jupyter Lab extension.
//






/**
 * Initialization data for the papyri-lab extension.
 */
const plugin = {
    id: 'papyri-lab:plugin',
    description: 'A JupyterLab extension for papyri',
    autoStart: true,
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_2__.INotebookTracker],
    activate: (app, palette, notebookTracker, settingRegistry, restorer) => {
        console.log('JupyterLab extension papyri-lab is activated!');
        if (settingRegistry) {
            settingRegistry
                .load(plugin.id)
                .then(settings => {
                console.log('papyri-lab settings loaded:', settings.composite);
            })
                .catch(reason => {
                console.error('Failed to load settings for papyri-lab.', reason);
            });
        }
        const newWidget = () => {
            // Create a blank content widget inside of a MainAreaWidget
            return new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content: new _widgets__WEBPACK_IMPORTED_MODULE_4__.PapyriPanel() });
        };
        let widget;
        // Track and restore the widget state
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'papyri'
        });
        const command = 'papyri:open';
        app.commands.addCommand(command, {
            label: 'Open Papyri Browser',
            execute: () => {
                // Regenerate the widget if disposed
                if (!widget || widget.isDisposed) {
                    widget = newWidget();
                }
                if (!tracker.has(widget)) {
                    // Track the state of the widget for later restoration
                    tracker.add(widget);
                }
                if (!widget.isAttached) {
                    // Attach the widget to the main work area if it's not there
                    app.shell.add(widget, 'main');
                }
                // Activate the widget
                app.shell.activateById(widget.id);
            }
        });
        // Add the command to the palette.
        palette.addItem({ command, category: 'Tutorial' });
        if (restorer) {
            restorer.restore(tracker, {
                command,
                name: () => 'papyri'
            });
        }
        const kernelSpy = new _kernelspy__WEBPACK_IMPORTED_MODULE_5__.KernelSpyModel(notebookTracker);
        kernelSpy.questionMarkSubmitted.connect((_, args) => {
            console.info('KSpy questionMarkSubmitted args:', args);
            if (args !== undefined) {
                console.info('DO your thing here.');
            }
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/kernelspy.js":
/*!**************************!*\
  !*** ./lib/kernelspy.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   KernelSpyModel: () => (/* binding */ KernelSpyModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
// This module implement an object that spies on the kernel messages
// to intercept documentation print request.


function isHeader(candidate) {
    return candidate.msg_id !== undefined;
}
/**
 * Model for a kernel spy.
 */
class KernelSpyModel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.VDomModel {
    // constructor(kernel?: Kernel.IKernelConnection | null) {
    constructor(notebookTracker, path) {
        console.log('notebook tracker constructed');
        super();
        this._log = [];
        this._kernel = null;
        this._messages = {};
        this._childLUT = {};
        this._roots = [];
        this._notebook = null;
        this._questionMarkSubmitted = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._notebookTracker = notebookTracker;
        this._notebookTracker.currentChanged.connect(this.onNotebookChanged, this);
        this.onNotebookChanged(undefined, { path });
    }
    onNotebookChanged(sender, args) {
        var _a, _b, _c, _d;
        console.log('notebook changed', args);
        // onNotebookChanged(notebookTracker: INotebookTracker, path?: string) {
        if (args.path) {
            this._notebook =
                (_a = this._notebookTracker.find(nb => nb.context.path === args.path)) !== null && _a !== void 0 ? _a : null;
        }
        else {
            this._notebook = this._notebookTracker.currentWidget;
        }
        if (this._notebook) {
            this.kernel =
                (_d = (_c = (_b = this._notebook.context.sessionContext) === null || _b === void 0 ? void 0 : _b.session) === null || _c === void 0 ? void 0 : _c.kernel) !== null && _d !== void 0 ? _d : null;
            this._notebook.context.sessionContext.kernelChanged.connect((_, args) => {
                this.kernel = args.newValue;
            });
        }
        else {
            this.kernel = null;
        }
    }
    clear() {
        this._log.splice(0, this._log.length);
        this._messages = {};
        this._childLUT = {};
        this._roots = [];
        this.stateChanged.emit(void 0);
    }
    get kernel() {
        return this._kernel;
    }
    set kernel(value) {
        if (this._kernel) {
            this._kernel.anyMessage.disconnect(this.onMessage, this);
        }
        this._kernel = value;
        if (this._kernel) {
            this._kernel.anyMessage.connect(this.onMessage, this);
        }
    }
    get log() {
        return this._log;
    }
    get tree() {
        return this._roots.map(rootId => {
            return this.getThread(rootId, false);
        });
    }
    depth(args) {
        if (args === null) {
            return -1;
        }
        let depth = 0;
        while ((args = this._findParent(args))) {
            ++depth;
        }
        return depth;
    }
    getThread(msgId, ancestors = true) {
        const args = this._messages[msgId];
        if (ancestors) {
            // Work up to root, then work downwards
            let root = args;
            let candidate;
            while ((candidate = this._findParent(root))) {
                root = candidate;
            }
            return this.getThread(root.msg.header.msg_id, false);
        }
        const childMessages = this._childLUT[msgId] || [];
        const childThreads = childMessages.map(childId => {
            return this.getThread(childId, false);
        });
        const thread = {
            args: this._messages[msgId],
            children: childThreads
        };
        return thread;
    }
    get questionMarkSubmitted() {
        return this._questionMarkSubmitted;
    }
    onMessage(sender, args) {
        const { msg } = args;
        this._log.push(args);
        this._messages[msg.header.msg_id] = args;
        const parent = this._findParent(args);
        if (parent === null) {
            this._roots.push(msg.header.msg_id);
        }
        else {
            const header = parent.msg.header;
            this._childLUT[header.msg_id] = this._childLUT[header.msg_id] || [];
            this._childLUT[header.msg_id].push(msg.header.msg_id);
        }
        // Log the kernel message here.
        if (args.direction === 'recv') {
            const msg = args.msg;
            if (msg.channel === 'shell' &&
                msg.content !== undefined &&
                msg.content.payload !== undefined &&
                msg.content.payload.length > 0) {
                console.log(msg.content.payload[0].data);
                console.log(msg.content.payload[0].data['x-vendor/papyri']);
                this._questionMarkSubmitted.emit(msg.content.payload[0].data['x-vendor/papyri']);
                console.log('QMS:', this._questionMarkSubmitted);
            }
        }
        this.stateChanged.emit(undefined);
    }
    _findParent(args) {
        if (isHeader(args.msg.parent_header)) {
            return this._messages[args.msg.parent_header.msg_id] || null;
        }
        return null;
    }
}


/***/ }),

/***/ "./lib/papyri-comp.js":
/*!****************************!*\
  !*** ./lib/papyri-comp.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   MyPapyri: () => (/* binding */ MyPapyri),
/* harmony export */   RENDERERS: () => (/* binding */ RENDERERS),
/* harmony export */   SearchContext: () => (/* binding */ SearchContext)
/* harmony export */ });
/* harmony import */ var myst_to_react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! myst-to-react */ "webpack/sharing/consume/default/myst-to-react/myst-to-react");
/* harmony import */ var myst_to_react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(myst_to_react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
// Global and other papyri-myst related componets



const SearchContext = (0,react__WEBPACK_IMPORTED_MODULE_1__.createContext)(async (query) => {
    return true;
});
const MyLink = ({ node }) => {
    const onSearch = (0,react__WEBPACK_IMPORTED_MODULE_1__.useContext)(SearchContext);
    const parts = node.url.split('/');
    const search_term = parts[parts.length - 1];
    const f = (q) => {
        onSearch(q);
    };
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("a", { onClick: () => f(search_term) },
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: node.children })));
};
const DefaultComponent = ({ node }) => {
    if (!node.children) {
        return react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, node.value);
    }
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "not-implemented" },
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: node.children })));
};
const MUnimpl = ({ node }) => {
    if (!node.children) {
        return react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, node.value);
    }
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "not-implemented unimpl" },
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: node.children })));
};
const Param = ({ node }) => {
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dt", null,
            node.param,
            ": ",
            node.type_),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dd", null, node.desc.map((sub) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: sub }))))));
};
const Parameters = ({ node }) => {
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dl", null, node.children.map((item) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: item })))));
};
const DefList = ({ node }) => {
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dl", null, node.children.map((item) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dt", null,
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: item.dt })),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("dd", null, item.dd.map((sub) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: sub })))))))));
};
// render a single parameter in a signature
const ParameterNodeRenderer = ({ node }) => {
    if (node.kind === '/') {
        return react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, "/");
    }
    let comp = [];
    let name = '';
    if (node.kind === 'VAR_POSITIONAL') {
        name = '*';
    }
    if (node.kind === 'VAR_KEYWORD') {
        name += '**';
    }
    name += node.name;
    comp = [react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, name)];
    if (node.annotation.type !== 'Empty') {
        comp.push(react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { className: "type-ann" }, ': ' + node.annotation.data));
    }
    if (node.default.type !== 'Empty') {
        comp.push(react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { className: "default-value" }, '=' + node.default.data));
    }
    return react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null, comp);
};
const SignatureRenderer = ({ node }) => {
    let prev = '';
    const acc = [];
    for (let i = 0; i < node.parameters.length; i++) {
        const p = node.parameters[i];
        if (p.kind !== 'POSITIONAL_ONLY' && prev === 'POSITIONAL_ONLY') {
            acc.push({ kind: '/', type: 'ParameterNode' });
        }
        prev = p.kind;
        acc.push(p);
    }
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("code", { className: "group signature" },
        node.kind.indexOf('async') !== -1 ||
            node.kind.indexOf('coroutine') !== -1
            ? 'async '
            : '',
        "def ",
        node.target_name,
        "(",
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null, acc.map((parameter, index, array) => {
            if (index + 1 === array.length) {
                return react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: parameter });
            }
            else {
                return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: parameter }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { className: "signature-separator" }, ', ')));
            }
        })),
        ')',
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { className: "ret-ann" }, node.return_annotation.data ? '-> ' + node.return_annotation.data : ''),
        ":"));
};
const Directive = ({ node }) => {
    const dom = node.domain !== null ? ':' + node.domain : '';
    const role = node.role !== null ? ':' + node.role + ':' : '';
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("code", { className: "not-implemented" },
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null,
                dom,
                role,
                "`",
                node.value,
                "`"))));
};
const LOC = {
    signature: SignatureRenderer,
    Directive: Directive,
    DefList: DefList,
    Parameters: Parameters,
    ParameterNode: ParameterNodeRenderer,
    Param: Param,
    MUnimpl: MUnimpl,
    DefaultComponent: DefaultComponent,
    link: MyLink
};
const RENDERERS = { ...myst_to_react__WEBPACK_IMPORTED_MODULE_0__.DEFAULT_RENDERERS, ...LOC };
function MyPapyri({ node }) {
    return react__WEBPACK_IMPORTED_MODULE_1___default().createElement(myst_to_react__WEBPACK_IMPORTED_MODULE_0__.MyST, { ast: node.children });
}


/***/ }),

/***/ "./lib/widgets.js":
/*!************************!*\
  !*** ./lib/widgets.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   PapyriPanel: () => (/* binding */ PapyriPanel)
/* harmony export */ });
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _papyri_comp__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./papyri-comp */ "./lib/papyri-comp.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _myst_theme_providers__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @myst-theme/providers */ "./node_modules/@myst-theme/providers/dist/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);





// this is a papyri react component that in the end should
// have navigation UI and a myst renderer to display the
// documentation.
//
// It is pretty bare bone for now, but might have a toolbar later.
//
// It would be nice to have this outside of the JupyterLab extension to be reusable
//
// I'm going to guess it will need some configuration hook for when we click on links.
//
//
class PapyriComponent extends (react__WEBPACK_IMPORTED_MODULE_2___default().Component) {
    constructor(props) {
        super(props);
        this.state = {
            possibilities: [],
            navs: [],
            root: {},
            searchterm: ''
        };
        this.state = {
            possibilities: [],
            navs: [],
            root: {},
            searchterm: ''
        };
    }
    setPossibilities(pos) {
        this.setState({ possibilities: pos });
    }
    setNavs(navs) {
        this.setState({ navs: navs });
    }
    setRoot(root) {
        this.setState({ root: root });
    }
    setSearchTerm(searchterm) {
        this.setState({ searchterm: searchterm });
    }
    async handleInputChange(event) {
        console.log('on change, this is', this);
        this.setSearchTerm(event.target.value);
        this.search(event.target.value);
    }
    async back() {
        this.state.navs.pop();
        const pen = this.state.navs.pop();
        if (pen !== undefined) {
            console.log('Setting search term', pen);
            await this.setSearchTerm(pen);
            console.log('... and searchg for ', pen);
            await this.search(pen);
        }
    }
    async search(query) {
        const res = await (0,_handler__WEBPACK_IMPORTED_MODULE_3__.requestAPI)('get-example', {
            body: query,
            method: 'post'
        });
        console.log('Got a response for', query, 'res.body=', res.body);
        // response has body (MyST–json if the query has an exact match)
        // and data if we have some close matches.
        if (res.body !== null) {
            this.setNavs([...this.state.navs, query]);
            this.setRoot(res.body);
            this.setPossibilities([]);
        }
        else {
            this.setRoot({});
            this.setPossibilities(res.data);
        }
    }
    async onClick(query) {
        console.log('On click trigger', query, 'this is', this);
        this.setSearchTerm(query);
        try {
            this.search(query);
        }
        catch (e) {
            console.error(e);
        }
        return false;
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement((react__WEBPACK_IMPORTED_MODULE_2___default().StrictMode), null,
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("input", { onChange: this.handleInputChange.bind(this), value: this.state.searchterm }),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("button", { onClick: this.back }, "Back"),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("ul", null, this.state.possibilities.map((e) => {
                return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement("a", { href: e, onClick: async () => {
                            await this.onClick(e);
                        } }, e)));
            })),
            react__WEBPACK_IMPORTED_MODULE_2___default().createElement("div", { className: "view" },
                react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_papyri_comp__WEBPACK_IMPORTED_MODULE_4__.SearchContext.Provider, { value: this.onClick.bind(this) },
                    react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_myst_theme_providers__WEBPACK_IMPORTED_MODULE_1__.ThemeProvider, { renderers: _papyri_comp__WEBPACK_IMPORTED_MODULE_4__.RENDERERS },
                        react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_papyri_comp__WEBPACK_IMPORTED_MODULE_4__.MyPapyri, { node: this.state.root }))))));
    }
}
// This seem to be the way to have an adapter between lumino and react, and
// allow to render react inside a JupyterLab panel
class PapyriPanel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor() {
        super();
        this.addClass('jp-ReactWidget');
        this.id = 'papyri-browser';
        this.title.label = 'Papyri browser';
        this.title.closable = true;
    }
    render() {
        return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(PapyriComponent, null);
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.454e946da84f62827b00.js.map