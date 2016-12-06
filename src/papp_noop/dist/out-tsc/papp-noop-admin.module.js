var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { PappNoopAdminComponent } from "./papp-noop-admin.component";
import { RouterModule } from "@angular/router";
/**
 * Created by peek on 5/12/16.
 */
export var pappRoutes = [
    {
        path: '',
        component: PappNoopAdminComponent
    },
    {
        path: '**',
        component: PappNoopAdminComponent
    }
];
var PappNoopAdminModule = (function () {
    function PappNoopAdminModule() {
    }
    PappNoopAdminModule = __decorate([
        NgModule({
            imports: [
                CommonModule,
                RouterModule.forChild(pappRoutes)],
            exports: [],
            providers: [],
            declarations: [PappNoopAdminComponent]
        }), 
        __metadata('design:paramtypes', [])
    ], PappNoopAdminModule);
    return PappNoopAdminModule;
}());
export default PappNoopAdminModule;
//# sourceMappingURL=/home/peek/project/papp_noop/src/papp_noop/admin/papp-noop-admin.module.js.map