import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-button',
  imports: [CommonModule],
  templateUrl: './button.component.html',
  styleUrl: './button.component.css'
})
export class ButtonComponent {
  @Input() url?: string;
  @Input() text!: string;
  @Input() type: string = 'submit';
  @Input() style: string = 'default';
  @Input() css?: string;
  @Input() id?: string;
  @Input() data_id?: number;
  @Input() project_id?: number;
}
