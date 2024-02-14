import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PaginaSenhaGeradaComponent } from './pagina-senha-gerada.component';

describe('PaginaSenhaGeradaComponent', () => {
  let component: PaginaSenhaGeradaComponent;
  let fixture: ComponentFixture<PaginaSenhaGeradaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PaginaSenhaGeradaComponent]
    });
    fixture = TestBed.createComponent(PaginaSenhaGeradaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
