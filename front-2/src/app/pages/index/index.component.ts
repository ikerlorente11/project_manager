import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ProjectComponent } from '../../project/project.component';
import { ButtonComponent } from '../../button/button.component';
import { environment } from '../../../environments/environment';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, ProjectComponent, ButtonComponent, HttpClientModule],
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {
  demo = false;
  projects: any;
  baseUrl = environment.baseUrl;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    if (typeof window !== 'undefined') {
      if (sessionStorage.getItem("disclaimer") === null && environment.demo) {
        this.demo = true;
      }

      this.http.get(environment.public_api_base_url + 'projects')
        .subscribe({
          next: (response) => {
            this.projects = response;
          },
          error: (error) => {
            console.error('Error al obtener los datos:', error);
          },
          complete: () => {
            console.log('La solicitud ha sido completada.');
          }
        });
    }
  }

  close() {
    this.demo = false;
    if (typeof window !== 'undefined') {
      sessionStorage.setItem("disclaimer", "false");
    }
  }
}
