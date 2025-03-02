import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IndexComponent } from './pages/index/index.component';
import { ProjectNewComponent } from './pages/project-new/project-new.component';

export const routes: Routes = [
    { path: '', component: IndexComponent },
    { path: 'project-new', component: ProjectNewComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes, { useHash: false })],
    exports: [RouterModule]
})

export class AppRoutingModule { }