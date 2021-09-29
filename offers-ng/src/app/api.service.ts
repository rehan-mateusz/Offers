import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class ApiService {

  base_url = 'http://localhost:8000/'
  http_headers = new HttpHeaders({'Content-Type': 'application/json'})
  constructor(private http: HttpClient) { }

  allOffers(): Observable<any>{
    return this.http.get(this.base_url + 'offers/', {headers: this.http_headers})
  }

  offerDetails(id): Observable<any>{
    return (this.http.get(this.base_url + 'offers/' + id + '/',
      {headers: this.http_headers}))
  }
}
