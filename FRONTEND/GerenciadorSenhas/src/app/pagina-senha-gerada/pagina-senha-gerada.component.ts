import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-pagina-senha-gerada',
  templateUrl: './pagina-senha-gerada.component.html',
  styleUrls: ['./pagina-senha-gerada.component.css']
})
export class PaginaSenhaGeradaComponent implements OnInit{
  hoje = new Date();
  senha!:string;
  constructor(private route: ActivatedRoute) { }
  ngOnInit(): void{
    this.route.queryParams.subscribe(params=>{
      this.senha=params['senha'] || '';
    })
  }
}
