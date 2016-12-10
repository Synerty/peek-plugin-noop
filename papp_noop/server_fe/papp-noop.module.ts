import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {PappNoopAdminComponent} from "./papp-noop-admin.component";
import {Routes, RouterModule} from "@angular/router";
/**
 * Created by peek on 5/12/16.
 *
 */

export const pappRoutes: Routes = [
    {
        path: '',
        component: PappNoopAdminComponent
    },
    {
        path: '**',
        component: PappNoopAdminComponent
    }

];

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(pappRoutes)],
    exports: [],
    providers: [],
    declarations: [PappNoopAdminComponent]
})
export default class PappNoopAdminModule {

}