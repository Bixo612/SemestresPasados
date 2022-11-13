--Prueba--Vicente Vasquez

--1 

CREATE USER usersum1 
IDENTIFIED BY C4ntr@S3gur4
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP;

--2 

Select Sucursal.Cod_Sucursal "Codigo sucursal", 
      Comuna.Nombre "Nombre comuna", 
      Count(Vendedor.Cod_Vendedor) "Cantidad vendedores",
      To_Char(Nvl(Sum(Venta.Valor_Total),0),'$999G999G999') "Total ventas", 
      To_Char(Nvl((Sum(Venta.Valor_Total)*0.47),0),'$999G999G999') "Utilidades"
From Sucursal Join Comuna On Sucursal.Comuna_Sucursal = Comuna.Cod_Comuna
     Left Outer Join Vendedor On Sucursal.Cod_Sucursal = Vendedor.Cod_Sucursal
     Left Outer Join Venta On Vendedor.Cod_Vendedor = Venta.Cod_Vendedor
Group By Sucursal.Cod_Sucursal, Comuna.Nombre
Order By Sucursal.Cod_Sucursal Asc;

--3

Select  Vendedor.Nom_Vendedor "Nombre",
        Vendedor.A_Paterno "Apellido",
        Vendedor.Salario "Salario",
        Extract (Year From Sysdate)-Extract (Year From Vendedor.Fech_Incorporacion) "Años trabajando",
        Rango_Sueldos.Porcentaje "% reajuste",
        (Vendedor.Salario)*(Rango_Sueldos.Porcentaje) "Valor final"
From Vendedor Join Rango_Sueldos 
On Extract (Year From Sysdate)-Extract (Year From Vendedor.Fech_Incorporacion) = Rango_Sueldos.Anios
Order By  Vendedor.Nom_Vendedor Asc; 

--4

Select Region.Nombre "Nombre region",
	 Count(Sucursal.Cod_Sucursal) "Cantidad sucursales",
     Count(Vendedor.Cod_Vendedor) "Cantidad trabajadores"
From Region Join Comuna On Region.Cod_Region = Comuna.Cod_Region
     Join Sucursal On Sucursal.Comuna_Sucursal = Comuna.Cod_Comuna
     Join Vendedor On Vendedor.Cod_Sucursal = Sucursal.Cod_Sucursal
Group By Region.Nombre
Having Count(Vendedor.Cod_Sucursal) < (Select Avg(Count(Cod_Sucursal))
                                       From Vendedor
                                       Group By Cod_Sucursal);

--5 

Select Nombre "Regiones sin sucursal"
From Region
Minus
Select Region.Nombre
From Region Right Outer Join Comuna On Region.Cod_Region =Comuna.Cod_Region
Right Outer Join Sucursal On Sucursal.Comuna_Sucursal = Comuna.Cod_Comuna;

--6

Select  Vendedor.Nom_Vendedor "Nombre",
        Vendedor.A_Paterno "Apellido",
        Vendedor.Direccion "Direccion", 
        Vendedor.Fechnac_Vendedor "Fecha nacimiento",
        Extract(Year From Vendedor.Fech_Incorporacion) "Fecha incorporacion",
        Vendedor.Nom_Vendedor||Vendedor.A_Paterno||Extract(Year From Vendedor.Fechnac_Vendedor)||
	   '@ventas.homeopaticos.cl' "Correo electrónico"       
From Vendedor Join Venta On Vendedor.Cod_Vendedor = Venta.Cod_Vendedor
Where Months_Between(Sysdate,Vendedor.Fech_Incorporacion) > 24
Group By    Vendedor.Nom_Vendedor,
            Vendedor.A_Paterno,
            Vendedor.Direccion, 
            Vendedor.Fechnac_Vendedor,
            Extract(Year From Vendedor.Fech_Incorporacion),
            Vendedor.Nom_Vendedor||Vendedor.A_Paterno||Extract(Year From Vendedor.Fechnac_Vendedor)||
	        '@ventas.homeopaticos.cl'
Having Count(Venta.Folio) < 6
Order By Vendedor.A_Paterno Asc, Vendedor.Nom_Vendedor Desc;

--7

Select * From Venta Intersect
Select * From Ventas;

-- 8 

COMMIT;

Insert Into Informe_Vendedores(Cod_Vendedor,Nom_Vendedor,A_Paterno,Direccion,
            Fech_Incorporacion,Salario,Folio,Fecha_Venta,Valor_Total)
    (
    Select Vendedor.Cod_Vendedor,Vendedor.Nom_Vendedor,Vendedor.A_Paterno,Vendedor.Direccion,
        Vendedor.Fech_Incorporacion,Vendedor.Salario,Ventas.Folio,Ventas.Fecha_Venta,
        Ventas.Valor_Total
    From Ventas Left Outer Join Vendedor 
        On Ventas.Cod_Vendedor = Vendedor.Cod_Vendedor
    Minus
    Select Vendedor.Cod_Vendedor,Vendedor.Nom_Vendedor,Vendedor.A_Paterno,Vendedor.Direccion,
        Vendedor.Fech_Incorporacion,Vendedor.Salario,Ventas.Folio,Ventas.Fecha_Venta,
        Ventas.Valor_Total
    From Ventas Join Vendedor 
        On Ventas.Cod_Vendedor = Vendedor.Cod_Vendedor
    );

--9

Update Producto
Set Precio_Producto = (Precio_Producto*1.025)
Where Cod_Producto In (Select Producto.Cod_Producto
                       From Producto, Product_Resp
                       Where Producto.Cod_Producto = Product_Resp.Cod_Producto 
                       And Producto.Precio_Producto != Product_Resp.Precio_Producto);
                       
ROLLBACK;