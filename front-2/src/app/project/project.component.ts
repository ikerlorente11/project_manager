import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-project',
  imports: [],
  templateUrl: './project.component.html',
  styleUrl: './project.component.css'
})
export class ProjectComponent {
  @Input() id!: number;
  @Input() name!: string;
  @Input() total_price!: number;
  @Input() unpaid!: string;

  get formattedPrice(): string {
    return this.total_price.toFixed(2); // Se asegura de que siempre tenga dos decimales
  }
}
