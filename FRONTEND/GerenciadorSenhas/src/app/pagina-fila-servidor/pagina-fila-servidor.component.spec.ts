import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PaginaFilaServidorComponent } from './pagina-fila-servidor.component';

describe('PaginaFilaServidorComponent', () => {
  let component: PaginaFilaServidorComponent;
  let fixture: ComponentFixture<PaginaFilaServidorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PaginaFilaServidorComponent]
    });
    fixture = TestBed.createComponent(PaginaFilaServidorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
