// simple demo vertex shader
// attribute variables
// www.lighthouse3d.com

varying vec4 out_Color;
varying vec4 position;

void main()
{
	vec4 p;
	p.xyz = gl_Vertex.xyz;
  p.w = 1.0;

  position = p;

  out_Color = gl_Color;
  gl_Position = gl_Vertex;
	gl_ModelViewProjectionMatrix * p;
}
