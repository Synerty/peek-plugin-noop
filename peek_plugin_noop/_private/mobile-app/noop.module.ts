import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {Routes} from "@angular/router";
import {RouterModule} from "@angular/router";

// Import the default route component
import {NoopComponent} from "./noop.component";
import {ConfigComponent} from "./config/config.component";


// Define the child routes for this plugin
export const pluginRoutes: Routes = [
    {
        path: '/config',
        component: ConfigComponent
    },
    {
        path: '',
        component: NoopComponent
    },
    {
        path: '**',
        component: NoopComponent
    }

];

// Define the root module for this plugin.
// This module is loaded by the lazy loader, what ever this defines is what is started.
// When it first loads, it will look up the routes and then select the component to load.
@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(pluginRoutes)
    ],
    exports: [],
    providers: [],
    declarations: [NoopComponent, ConfigComponent]
})
export class NoopModule {}
