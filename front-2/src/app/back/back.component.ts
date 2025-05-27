import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-back',
  imports: [],
  templateUrl: './back.component.html',
  styleUrl: './back.component.css'
})
export class BackComponent {
  @Input() url!: string;
}
