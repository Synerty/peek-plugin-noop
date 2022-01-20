import { Component } from "@angular/core";
import { NgLifeCycleEvents } from "@synerty/vortexjs";

@Component({
    selector: "plugin-noop-mobile-config",
    templateUrl: "config.component.mweb.html",
})
export class ConfigComponent extends NgLifeCycleEvents {
    constructor() {
        super();
    }
}
