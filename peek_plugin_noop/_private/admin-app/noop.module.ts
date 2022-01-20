import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { NoopComponent } from "./noop.component";
import { RouterModule, Routes } from "@angular/router";

export const pluginRoutes: Routes = [
    {
        path: "",
        component: NoopComponent,
    },
];

@NgModule({
    imports: [CommonModule, RouterModule.forChild(pluginRoutes)],
    exports: [],
    providers: [],
    declarations: [NoopComponent],
})
export class NoopModule {}
