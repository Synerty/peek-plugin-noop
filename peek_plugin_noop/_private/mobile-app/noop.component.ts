import { Component } from "@angular/core";
import { extend, NgLifeCycleEvents, VortexService } from "@synerty/vortexjs";
import { noopFilt } from "@peek/peek_plugin_noop/_private";
import {
    BalloonMsgLevel,
    BalloonMsgService,
    BalloonMsgType,
} from "@synerty/peek-plugin-base-js";

@Component({
    selector: "plugin-noop-mobile",
    templateUrl: "noop.component.mweb.html",
})
export class NoopComponent extends NgLifeCycleEvents {
    date: string = "No data yet";
    stopped: boolean = false;

    private filt = extend(
        {
            key: "sendDate",
        },
        noopFilt
    );

    constructor(
        vortexService: VortexService,
        private balloonMsg: BalloonMsgService
    ) {
        super();

        let loader = vortexService.createTupleLoader(this, this.filt);
        loader.observable.subscribe((tuples) => {
            // Update our value
            this.date = tuples[0];
        });

        this.onDestroyEvent.subscribe(() => {
            this.stopped = true;
        });

        let loadAgain = () => {
            if (this.stopped) return;

            // Schedule a reload in 1 second
            setTimeout(() => {
                loadAgain();
                loader.load();
            }, 2000);
        };

        loadAgain();
    }

    showSuccessMsgClicked() {
        this.balloonMsg.showSuccess("You have clicked the button.", "/");
    }

    showInfoConfirm() {
        let p = this.balloonMsg.showMessage(
            "This is a info confirm.",
            BalloonMsgLevel.Info,
            BalloonMsgType.Confirm
        );
    }
}
