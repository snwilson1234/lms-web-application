import { Component, Input, OnInit } from "@angular/core";
import { Page } from "../../enum/page.enum";
import { CommonModule } from "@angular/common";
import { RouterLink, RouterLinkActive, RouterOutlet } from "@angular/router";
import { MatIconModule } from '@angular/material/icon';

@Component({
    selector: 'app-header',
    standalone: true,
    imports: [
        CommonModule,
        MatIconModule,
        RouterOutlet,
        RouterLink,
        RouterLinkActive
    ],
    templateUrl: 'app-header.component.html',
    styleUrl: 'app-header.component.scss',
    providers: []
})
export class AppHeaderComponent implements OnInit {
    readonly Page = Page;
    @Input() title: string = "";

    ngOnInit(): void {

    }

}