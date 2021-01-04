import { Component } from "@angular/core"
import { NgLifeCycleEvents, VortexService } from "@synerty/vortexjs"
import { noopFilt } from "@peek/peek_plugin_noop/_private"
import { extend } from "@synerty/vortexjs"
import {
    BalloonMsgService,
    BalloonMsgLevel,
    BalloonMsgType
} from "@synerty/peek-plugin-base-js"

@Component({
    selector: "plugin-noop-mobile-config",
    templateUrl: "config.component.mweb.html"
})
export class ConfigComponent extends NgLifeCycleEvents {
    
    constructor() {
        super()
    }
    
}
