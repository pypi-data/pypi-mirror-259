"use strict";
(self["webpackChunkmyextension"] = self["webpackChunkmyextension"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Initialization data for the myextension extension.
 */
const plugin = {
    id: 'myextension:plugin',
    description: 'A JupyterLab extension.',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: async (app, palette) => {
        console.log('JupyterLab extension jupyterlab_apod is activated!');
        console.log('我修改了');
        // Define a widget creator function,
        // then call it to make a new widget
        const newWidget = async () => {
            // Create a blank content widget inside of a MainAreaWidget
            const content = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget();
            const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget({ content });
            widget.id = 'znn-test';
            widget.title.label = '测试随机图片';
            widget.title.closable = true;
            // Add an image element to the content
            let img = document.createElement('img');
            content.node.appendChild(img);
            // Get a random date string in YYYY-MM-DD format
            function randomDate() {
                const start = new Date(2010, 1, 1);
                const end = new Date();
                const randomDate = new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
                return randomDate.toISOString().slice(0, 10);
            }
            // Fetch info about a random picture
            const response = await fetch(`https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=${randomDate()}`);
            const data = (await response.json());
            if (data.media_type === 'image') {
                // Populate the image
                img.src = data.url;
                img.title = data.title;
            }
            else {
                console.log('Random APOD was not a picture.');
            }
            return widget;
        };
        let widget = await newWidget();
        // Add an application command
        const command = 'znn:open';
        app.commands.addCommand(command, {
            label: '测试一下',
            execute: async () => {
                // Regenerate the widget if disposed
                if (widget.isDisposed) {
                    widget = await newWidget();
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
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.352c32bde25f0060041a.js.map