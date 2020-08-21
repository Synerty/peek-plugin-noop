import { NgModule, OnDestroy } from "@angular/core";
import { HttpClientModule } from "@angular/common/http";
import { PluginNoopClientRootService } from "./plugin-noop-root.service";
import { CommonModule } from "@angular/common";
import { FormsModule } from "@angular/forms";
import { NzIconModule } from "ng-zorro-antd/icon";
import { MobileRootComponent } from "./root-component/root.component";

/** Client Root Module
 *
 * This module will be loaded by peek-mobile when the app loads.
 * There will be one instance of it, and it be around for the life of the app.
 *
 * Configure this in plugin_package.json
 */

@NgModule({
    imports: [CommonModule, FormsModule, NzIconModule, HttpClientModule],
    exports: [MobileRootComponent],
    providers: [],
    declarations: [MobileRootComponent],
})
export class PluginNoopClientRootModule implements OnDestroy {
    private static instanceCount = 0;
    private instanceIndex;

    constructor(private noopRootService: PluginNoopClientRootService) {
        this.instanceIndex = PluginNoopClientRootModule.instanceCount++;
        console.log(
            "peek-plugin-noop - PluginNoopClientRootModule LOADED #" +
                this.instanceIndex
        );
    }

    ngOnDestroy() {
        console.log(
            "peek-plugin-noop - PluginNoopClientRootModule DESTROYED #" +
                this.instanceIndex
        );
    }
}
