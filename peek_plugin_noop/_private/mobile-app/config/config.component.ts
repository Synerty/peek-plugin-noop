import {Component} from "@angular/core";
import {ComponentLifecycleEventEmitter, VortexService} from "@synerty/vortexjs";
import {noopFilt} from "@peek/peek_plugin_noop/_private";
import {extend} from "@synerty/vortexjs";
import {Ng2BalloonMsgService, UsrMsgLevel, UsrMsgType} from "@synerty/ng2-balloon-msg";

@Component({
    selector: 'plugin-noop-mobile-config',
    templateUrl: 'config.component.mweb.html',
    moduleId: module.id
})
export class ConfigComponent extends ComponentLifecycleEventEmitter {


    constructor() {
        super();
    }

}