import {Component} from "@angular/core";
import {ComponentLifecycleEventEmitter} from "@synerty/vortexjs";

@Component({
    selector: 'plugin-noop-mobile-root-component',
    templateUrl: 'root.component.mweb.html',
    moduleId: module.id
})
export class MobileRootComponent extends ComponentLifecycleEventEmitter {

    constructor() {
        super();
    }

}