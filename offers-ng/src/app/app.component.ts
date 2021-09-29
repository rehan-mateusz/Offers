import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  offers = [];
  detailsList = new Dictionary()

  constructor(private api:ApiService) {
    this.getOffers();
  }
  getOffers = () => {
    this.api.allOffers().subscribe(data => {this.offers = data})
  }
  getOfferDetails = (id) => {
    this.api.offerDetails(id).subscribe(data => {
      this.detailsList.set(id, data)})
  }
}
export class Dictionary {
      items = {};
      constructor() {
        this.items = {};
      }
      public has(key) {
        return key in this.items;
      }
      public set(key,value) {
        this.items[key] = value;
      }
      public get(key) {
        return this.items[key];
      }
      public delete(key) {
        if( this.has(key) ){
          delete this.items[key]
          return true;
        }
        return false;
      }
    }
