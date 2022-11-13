Select Vendedor.Nom_Vendedor "Nombre", Vendedor.A_Paterno "Apellido",
       Vendedor.Direccion "Direccion", Vendedor.Fechnac_Vendedor "Fecha nacimiento",
       Vendedor.Fech_Incorporacion "Fecha incorporacion",
       Extract(Year From Sysdate)-Extract(Year From Vendedor.Fech_Incorporacion)
	   ||Substr(Vendedor.A_Paterno,-2)||Extract(Year From Vendedor.Fechnac_Vendedor)||
	   '@ventas.homeopaticos.cl' "Correo electrónico"
From Vendedor Join Venta On Vendedor.Cod_Vendedor = Venta.Cod_Vendedor
Where Months_Between(Sysdate,Vendedor.Fech_Incorporacion) > 24
Group By Vendedor.Nom_Vendedor, Vendedor.A_Paterno, Vendedor.Direccion, 
         Vendedor.Fechnac_Vendedor,Vendedor.Fech_Incorporacion, Extract(Year From Sysdate)-Extract(Year From Vendedor.Fech_Incorporacion),
       Extract(Year From Sysdate)-Extract(Year From Vendedor.Fech_Incorporacion)
	   ||Substr(Vendedor.A_Paterno,-2)||Extract(Year From Vendedor.Fechnac_Vendedor)||
	   '@ventas.homeopaticos.cl'
Having Count(Venta.Folio) < 3
Order By Vendedor.A_Paterno Desc, Vendedor.Nom_Vendedor Asc;

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