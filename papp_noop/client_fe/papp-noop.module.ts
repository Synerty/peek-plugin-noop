import {CommonModule} from "@angular/common";
import {NgModule} from "@angular/core";
import {PappNoopClientComponent} from "./papp-noop-client.component";
import {Routes, RouterModule} from "@angular/router";
/**
 * Created by peek on 5/12/16.
 */

export const pappRoutes: Routes = [
    {
        path: '',
        component: PappNoopClientComponent
    },
    {
        path: '**',
        component: PappNoopClientComponent
    }

];

@NgModule({
    imports: [
        CommonModule,
        RouterModule.forChild(pappRoutes)],
    exports: [],
    providers: [],
    declarations: [PappNoopClientComponent]
})
export default class PappNoopClientModule {

}