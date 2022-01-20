import { Injectable, OnDestroy } from "@angular/core";

/** Client Root Service
 *
 * This service will be loaded by peek-field-app when the app laods.
 * There will be one instance of it, and it be around for the life of the app.
 *
 * Configure this in plugin_package.json
 */

@Injectable()
export class PluginNoopClientRootService implements OnDestroy {
    private static instanceCount = 0;
    private instanceIndex;

    constructor() {
        this.instanceIndex = PluginNoopClientRootService.instanceCount++;
        console.log(
            "peek-plugin-noop - PluginNoopClientRootService LOADED #" +
                this.instanceIndex
        );
    }

    ngOnDestroy() {
        console.log(
            "peek-plugin-noop - PluginNoopClientRootService DESTROYED #" +
                this.instanceIndex
        );
    }
}
