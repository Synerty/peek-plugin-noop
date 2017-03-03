import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {PluginNoopAdminComponent} from "./plugin-noop-admin.component";
import {Routes, RouterModule} from "@angular/router";
/**
 * Created by peek on 5/12/16.
 *
 */

export const pluginRoutes: Routes = [
    {
        path: '',
        component: PluginNoopAdminComponent
    }

];

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(pluginRoutes)],
    exports: [],
    providers: [],
    declarations: [PluginNoopAdminComponent]
})
export default class PluginNoopAdminModule {

}