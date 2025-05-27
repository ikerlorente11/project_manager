import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Project } from '../models/project';
import { ButtonComponent } from '../button/button.component';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-project-form',
  imports: [CommonModule, ButtonComponent],
  templateUrl: './project-form.component.html',
  styleUrl: './project-form.component.css'
})
export class ProjectFormComponent {
  @Input() project?: Project;

  method = this.project ? "PUT" : "POST";

  // Construct the URL for the API request based on whether a project exists
  url = this.project
      ? `${environment.baseUrl}projects/${this.project.id}`  // URL for updating an existing project
      : `${environment.baseUrl}projects`;     

  ngAfterViewInit() {
    document.getElementById("saveProject")?.addEventListener("click", async (event) => {
      event.preventDefault(); // Prevent the default form submission behavior
      console.log("Guardando proyecto...");
      // // Get the form element by its ID
      // const form = document.getElementById("projectForm") as HTMLFormElement;

      // if(form){
      //   // Create a FormData object from the form
      //   const formData = new FormData(form);
      //   // Convert the FormData to a JSON object
      //   const jsonData = Object.fromEntries(formData.entries());

      //   // Determine the HTTP method based on the form's method attribute
      //   const method = this.project ? "PUT" : "POST";
      //   // Get the action URL from the form
      //   const action = this.url;

      //   try {
      //       // Send a fetch request to the server with the form data
      //       const response = await fetch(action, {
      //           method: method, // Use the determined method (POST or PUT)
      //           headers: {
      //               "Content-Type": "application/json", // Set the content type to JSON
      //           },
      //           body: JSON.stringify(jsonData), // Convert the JSON object to a string
      //       });

      //       // Check if the response is OK (status in the range 200-299)
      //       if (response.ok) {
      //           // Get the base URL from a data attribute on the body
      //           const baseUrl = document.body.getAttribute("data-base-url");
      //           if (this.method == "post") {
      //               console.log("Proyecto guardado exitosamente."); // Log success message for saving
      //               // Redirect to the base URL
      //               window.location.href = `${baseUrl}`;
      //           } else {
      //               console.log("Proyecto actualizado exitosamente."); // Log success message for updating
      //               // Redirect to the project's page
      //               window.location.href = `${baseUrl}projects/` + jsonData['id'];
      //           }
      //       } else {
      //           console.error("Error en la respuesta del servidor."); // Log error if response is not OK
      //       }
      //   } catch (error) {
      //       console.error("Error en la petición:", error); // Log any errors that occur during the fetch
      //   }
      // }
    });
  }
}
