import {OnInit} from "@angular/core";
import {PeekComponent} from "@synerty/peek-web-ns";

@PeekComponent({
    selector: 'plugin-noop-admin',
    templateUrl: 'plugin-noop-client.component.web.html',
    moduleFilename: module.filename
})
export class PluginNoopClientComponent implements OnInit {

    ngOnInit() {

    }
}
