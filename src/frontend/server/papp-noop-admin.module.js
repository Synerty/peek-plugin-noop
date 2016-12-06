"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var common_1 = require("@angular/common");
var core_1 = require("@angular/core");
var papp_noop_admin_component_1 = require("./papp-noop-admin.component.js");
var router_1 = require("@angular/router");
/**
 * Created by peek on 5/12/16.
 */
exports.pappRoutes = [
    {
        path: '',
        component: papp_noop_admin_component_1.PappNoopAdminComponent
    },
    {
        path: '**',
        component: papp_noop_admin_component_1.PappNoopAdminComponent
    }
];
var PappNoopAdminModule = (function () {
    function PappNoopAdminModule() {
    }
    PappNoopAdminModule = __decorate([
        core_1.NgModule({
            imports: [
                common_1.CommonModule,
                router_1.RouterModule.forChild(exports.pappRoutes)],
            exports: [],
            providers: [],
            declarations: [papp_noop_admin_component_1.PappNoopAdminComponent]
        })
    ], PappNoopAdminModule);
    return PappNoopAdminModule;
}());
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = PappNoopAdminModule;
