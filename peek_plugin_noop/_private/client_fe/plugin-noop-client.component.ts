import {Component, OnInit} from "@angular/core";
import {PeekComponent} from "@synerty/peek-web-ns";

@PeekComponent({
    selector: 'plugin-noop-admin',
    templateUrl: 'plugin-noop-client.component.web.html',
    templateNsUrl: 'peek_plugin_noop/plugin-noop-client.component.ns.html'
})
export class PluginNoopClientComponent  implements OnInit {

    ngOnInit() {

    }
}
