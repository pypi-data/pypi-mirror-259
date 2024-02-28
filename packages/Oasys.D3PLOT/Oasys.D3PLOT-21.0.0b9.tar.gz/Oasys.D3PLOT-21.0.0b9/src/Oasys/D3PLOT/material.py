import Oasys.gRPC


# Metaclass for static properties and constants
class MaterialType(type):

    def __getattr__(cls, name):

        raise AttributeError


class Material(Oasys.gRPC.OasysItem, metaclass=MaterialType):
    _props = {'include', 'index', 'label', 'model', 'name', 'title', 'type'}


    def __del__(self):
        if not Oasys.D3PLOT._connection:
            return

        Oasys.D3PLOT._connection.destructor(self.__class__.__name__, self._handle)


    def __getattr__(self, name):
# If one of the properties we define then get it
        if name in Material._props:
            return Oasys.D3PLOT._connection.instanceGetter(self.__class__.__name__, self._handle, name)

        raise AttributeError


    def __setattr__(self, name, value):
# If one of the properties we define then set it
        if name in Material._props:
            Oasys.D3PLOT._connection.instanceSetter(self.__class__.__name__, self._handle, name, value)
            return

# Set the property locally
        self.__dict__[name] = value


# Static methods
    def First(model):
        """
        Returns the first material in the model (or None if there are no materials in the model)

        Parameters
        ----------
        model : Model
            Model to get first material in

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "First", model)

    def FlagAll(model, flag):
        """
        Flags all of the materials in the model with a defined flag

        Parameters
        ----------
        model : Model
            Model that all the materials will be flagged in
        flag : Flag
            Flag (see AllocateFlag) to set on the materials

        Returns
        -------
        None
            No return value
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "FlagAll", model, flag)

    def GetAll(model):
        """
        Gets all of the materials in the model

        Parameters
        ----------
        model : Model
            Model that all the materials are in

        Returns
        -------
        array
            Array of :py:class:`Material <Material>` objects
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "GetAll", model)

    def GetFlagged(model, flag):
        """
        Gets all of the materials in the model flagged with a defined flag

        Parameters
        ----------
        model : Model
            Model that the flagged materials are in
        flag : Flag
            Flag (see AllocateFlag) set on the materials to get

        Returns
        -------
        array
            Array of :py:class:`Material <Material>` objects
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "GetFlagged", model, flag)

    def GetFromID(model, label):
        """
        Returns the Material object for material in model with label (or None if it does not exist)

        Parameters
        ----------
        model : Model
            Model to get material in
        label : integer
            The LS-DYNA label for the material in the model

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "GetFromID", model, label)

    def GetFromIndex(model, index):
        """
        Returns the Material object for material in model with index (or None if it does not exist)

        Parameters
        ----------
        model : Model
            Model to get material in
        index : integer
            The D3PLOT internal index in the model for material

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "GetFromIndex", model, index)

    def Last(model):
        """
        Returns the last material in the model (or None if there are no materials in the model)

        Parameters
        ----------
        model : Model
            Model to get last material in

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "Last", model)

    def Total(model):
        """
        Returns the total number of materials in the model

        Parameters
        ----------
        model : Model
            Model to get total in

        Returns
        -------
        integer
            The number of materials
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "Total", model)

    def UnflagAll(model, flag):
        """
        Unsets a defined flag on all of the materials in the model

        Parameters
        ----------
        model : Model
            Model that the defined flag for all materials will be unset in
        flag : Flag
            Flag (see AllocateFlag) to unset on the materials

        Returns
        -------
        None
            No return value
        """
        return Oasys.D3PLOT._connection.classMethod(__class__.__name__, "UnflagAll", model, flag)



# Instance methods
    def ClearFlag(self, flag):
        """
        Clears a flag on a material

        Parameters
        ----------
        flag : Flag
            Flag (see AllocateFlag) to clear on the material

        Returns
        -------
        None
            No return value
        """
        return Oasys.D3PLOT._connection.instanceMethod(self.__class__.__name__, self._handle, "ClearFlag", flag)

    def Flagged(self, flag):
        """
        Checks if the material is flagged or not

        Parameters
        ----------
        flag : Flag
            Flag (see AllocateFlag) to test on the material

        Returns
        -------
        boolean
            True if flagged, False if not
        """
        return Oasys.D3PLOT._connection.instanceMethod(self.__class__.__name__, self._handle, "Flagged", flag)

    def Next(self):
        """
        Returns the next material in the model (or None if there is not one)

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.instanceMethod(self.__class__.__name__, self._handle, "Next")

    def Previous(self):
        """
        Returns the previous material in the model (or None if there is not one)

        Returns
        -------
        Material
            Material object
        """
        return Oasys.D3PLOT._connection.instanceMethod(self.__class__.__name__, self._handle, "Previous")

    def SetFlag(self, flag):
        """
        Sets a flag on a material

        Parameters
        ----------
        flag : Flag
            Flag (see AllocateFlag) to set on the material

        Returns
        -------
        None
            No return value
        """
        return Oasys.D3PLOT._connection.instanceMethod(self.__class__.__name__, self._handle, "SetFlag", flag)

