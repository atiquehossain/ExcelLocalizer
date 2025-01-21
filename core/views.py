from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorldView(APIView):
    """
    This is the Hello World API view.
    """
    @swagger_auto_schema(
        operation_description="This endpoint returns a Hello World message.",
        responses={200: "Hello, World!"}
    )
    def get(self, request):
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)




class FlutterHomeCodeView(APIView):



  @swagger_auto_schema(
      operation_description="This endpoint returns the 'home' portion of the Flutter code in a structured JSON format.",
      responses={200: "JSON with Flutter home code"}
  )
  def get(self, request):
      # Structuring the widget data in a clear and readable format with improvements
      flutter_home_code = {
          "flutter_home_code": {
              "type": "Scaffold",
              "backgroundColor": "#f4f4f4",  # Light background color for the whole screen
              "appBar": {
                  "type": "AppBar",
                  "backgroundColor": "#6200EE",  # AppBar with a nice color
                  "title": {
                      "type": "Text",
                      "text": "Resume",
                      "style": {
                          "color": "#FFFFFF",  # White title color
                          "fontSize": 22,
                          "fontWeight": "bold"
                      }
                  }
              },
              "body": {
                  "type": "Center",  # Center everything
                  "child": {
                      "type": "Padding",  # Add padding around the body content
                      "padding": {
                          "top": 20,
                          "left": 20,
                          "right": 20,
                          "bottom": 20
                      },
                      "child": {
                          "type": "Column",
                          "mainAxisAlignment": "center",  # Vertically center the content
                          "crossAxisAlignment": "center",  # Horizontally center the content
                          "children": [
                              {
                                  "type": "CircleAvatar",
                                  "backgroundImage": {
                                      "type": "NetworkImage",
                                      "url": "https://i.pinimg.com/280x280_RS/0e/df/b6/0edfb6a1f3a458cf1d01d03012717ac3.jpg"
                                  },
                                  "radius": 60
                              },
                              {
                                  "type": "SizedBox",  # Space between avatar and text
                                  "height": 20
                              },
                              {
                                  "type": "Text",
                                  "text": "Atique Hossain",
                                  "style": {
                                      "fontSize": 28,
                                      "fontWeight": "bold",
                                      "color": "#333333"
                                  }
                              },
                              {
                                  "type": "Text",
                                  "text": "Software Engineer",
                                  "style": {
                                      "fontSize": 20,
                                      "fontStyle": "italic",
                                      "color": "#666666"
                                  }
                              },
                              {
                                  "type": "SizedBox",  # Space between role and email
                                  "height": 10
                              },
                              {
                                  "type": "Text",
                                  "text": "Email: john.doe@example.com",
                                  "style": {
                                      "fontSize": 16,
                                      "color": "#333333"
                                  }
                              },
                              {
                                  "type": "SizedBox",  # Space between email and buttons
                                  "height": 20
                              },
                              {
                                  "type": "Row",  # Button row
                                  "mainAxisAlignment": "center",  # Center buttons horizontally
                                  "children": [
                                      {
                                          "type": "ElevatedButton",
                                          "child": {
                                              "type": "Text",
                                              "text": "LinkedIn",
                                              "style": {
                                                  "color": "#FFFFFF"
                                              }
                                          },
                                          "onPressed": {"print(""https://www.linkedin.com/in/atique-hossain/"")"},
                                          "style": {
                                              "backgroundColor": "#6200EE",
                                              "padding": {"vertical": 10, "horizontal": 20},
                                              "shape": {"type": "RoundedRectangleBorder", "borderRadius": 15}
                                          }
                                      },
                                      {
                                          "type": "SizedBox",  # Space between the two buttons
                                          "width": 10
                                      },
                                      {
                                          "type": "ElevatedButton",
                                          "child": {
                                              "type": "Text",
                                              "text": "GitHub",
                                              "style": {
                                                  "color": "#FFFFFF"
                                              }
                                          },
                                          "onPressed": "open_github",
                                          "style": {
                                              "backgroundColor": "#333333",
                                              "padding": {"vertical": 10, "horizontal": 20},
                                              "shape": {"type": "RoundedRectangleBorder", "borderRadius": 15}
                                          }
                                      }
                                  ]
                              }
                          ]
                      }
                  }
              }
          }
      }

      # Returning the structured JSON with HTTP 200 status
      return Response(flutter_home_code, status=status.HTTP_200_OK)

