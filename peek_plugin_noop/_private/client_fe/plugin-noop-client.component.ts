import {PeekComponent} from "@synerty/peek-web-ns";
import {
    VortexService,
    ComponentLifecycleEventEmitter,
    TupleLoader
} from "@synerty/vortexjs";

@PeekComponent({
    selector: 'plugin-noop-admin',
    templateUrl: 'plugin-noop-client.component.web.html',
    moduleFilename: module.filename
})
export class PluginNoopClientComponent extends ComponentLifecycleEventEmitter {

    date: string = "No data yet";
    stopped : boolean = false;

    private filt = {
        "plugin": "peek_plugin_noop",
        "key": "sendDate"
    };

    constructor(vortexService: VortexService) {
        super();

        let loader = vortexService.createTupleLoader(this, this.filt);
        loader.observable
            .subscribe(tuples => {
                // Update our value
                this.date = tuples[0];

            });

        this.onDestroyEvent.subscribe(() => {this.stopped=true;});

        let loadAgain = () => {
            if (this.stopped)
                return;

            // Schedule a reload in 1 second
            setTimeout(() => {
                loadAgain();
                loader.load()
            }, 2000);
        };

        loadAgain();
    }


}