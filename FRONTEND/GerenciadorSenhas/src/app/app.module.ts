import { HttpClient } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginServidorComponent } from './login-servidor/login-servidor.component';
import { CadastroUsuarioComponent } from './cadastro-usuario/cadastro-usuario.component';
import { PaginaSenhaGeradaComponent } from './pagina-senha-gerada/pagina-senha-gerada.component';
import { PaginaFilaServidorComponent } from './pagina-fila-servidor/pagina-fila-servidor.component';
import { routing } from './app.routing';
import{ HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { SenhaComponent } from './senha/senha.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginServidorComponent,
    CadastroUsuarioComponent,
    PaginaSenhaGeradaComponent,
    PaginaFilaServidorComponent,
    SenhaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    routing,
    HttpClientModule,
    FormsModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
