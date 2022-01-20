import { Component } from "@angular/core";
import { NgLifeCycleEvents } from "@synerty/vortexjs";

@Component({
    selector: "plugin-noop-mobile-root-component",
    templateUrl: "root.component.mweb.html",
})
export class MobileRootComponent extends NgLifeCycleEvents {
    constructor() {
        super();
    }
}
