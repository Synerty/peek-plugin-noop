import {NgModule, OnDestroy} from "@angular/core";
import {PluginNoopClientRootService} from "./plugin-noop-root.service";

/** Client Root Module
 *
 * This module will be loaded by peek-client-fe when the app laods.
 * There will be one instance of it, and it be around for the life of the app.
 *
 * Configure this in plugin_package.json
 */

@NgModule({})
export class PluginNoopClientRootModule implements OnDestroy {
    private static instanceCount = 0;
    private instanceIndex;

    constructor(private noopRootService: PluginNoopClientRootService) {
        this.instanceIndex = PluginNoopClientRootModule.instanceCount++;
        console.log("peek-plugin-noop - PluginNoopClientRootModule LOADED #"
            + this.instanceIndex);
    }

    ngOnDestroy() {
        console.log("peek-plugin-noop - PluginNoopClientRootModule DESTROYED #"
            + this.instanceIndex);
    }
}