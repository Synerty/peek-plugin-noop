import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {PluginNoopClientComponent} from "./plugin-noop-client.component";
import {Routes, RouterModule} from "@angular/router";
import {PeekPluginMenuI, PeekPluginMenuItem} from "interfaces/PeekPluginMenuItem";
/**
 * Created by peek on 5/12/16.
 */


export const pluginRoutes: Routes = [
    {
        path: '',
        component: PluginNoopClientComponent
    },
    {
        path: '**',
        component: PluginNoopClientComponent
    }

];

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(pluginRoutes)],
    exports: [],
    providers: [],
    declarations: [PluginNoopClientComponent]
})
export default class PluginNoopClientModule implements PeekPluginMenuI {
    menuRoot(): PeekPluginMenuItem {
        return {
            name: "Noop",
            url: "subItems",
            subItems: []
        }
    }
}