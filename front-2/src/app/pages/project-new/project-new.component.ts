import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BackComponent } from '../../back/back.component';
import { HeaderComponent } from '../../header/header.component';
import { ProjectFormComponent } from '../../project-form/project-form.component';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-project-new',
  imports: [RouterOutlet, BackComponent, HeaderComponent, ProjectFormComponent],
  templateUrl: './project-new.component.html',
  styleUrl: './project-new.component.css'
})
export class ProjectNewComponent {
  baseUrl = environment.baseUrl;
}
