import Oasys.gRPC


# Metaclass for static properties and constants
class InterfaceSpringbackType(type):
    _consts = {'EXCLUDE', 'LSDYNA', 'NASTRAN', 'NIKE3D', 'SEAMLESS'}

    def __getattr__(cls, name):
        if name in InterfaceSpringbackType._consts:
            return Oasys.PRIMER._connection.classGetter(cls.__name__, name)

        raise AttributeError


class InterfaceSpringback(Oasys.gRPC.OasysItem, metaclass=InterfaceSpringbackType):
    _props = {'cflag', 'exists', 'fsplit', 'ftensr', 'ftype', 'include', 'intstrn', 'ncyc', 'ndflag', 'nexclude', 'nnodes', 'nothickness', 'nshv', 'nthhsv', 'optcard', 'psid', 'sldo', 'type'}
    _rprops = {'model'}


    def __del__(self):
        if not Oasys.PRIMER._connection:
            return

        Oasys.PRIMER._connection.destructor(self.__class__.__name__, self._handle)


    def __getattr__(self, name):
# If one of the properties we define then get it
        if name in InterfaceSpringback._props:
            return Oasys.PRIMER._connection.instanceGetter(self.__class__.__name__, self._handle, name)

# If one of the read only properties we define then get it
        if name in InterfaceSpringback._rprops:
            return Oasys.PRIMER._connection.instanceGetter(self.__class__.__name__, self._handle, name)

        raise AttributeError


    def __setattr__(self, name, value):
# If one of the properties we define then set it
        if name in InterfaceSpringback._props:
            Oasys.PRIMER._connection.instanceSetter(self.__class__.__name__, self._handle, name, value)
            return

# If one of the read only properties we define then error
        if name in InterfaceSpringback._rprops:
            raise AttributeError

# Set the property locally
        self.__dict__[name] = value


# Constructor
    def __init__(self, model, type, psid=Oasys.gRPC.defaultArg, nshv=Oasys.gRPC.defaultArg, ftype=Oasys.gRPC.defaultArg, ftensr=Oasys.gRPC.defaultArg, nthhsv=Oasys.gRPC.defaultArg, intstrn=Oasys.gRPC.defaultArg, optcard=Oasys.gRPC.defaultArg, sldo=Oasys.gRPC.defaultArg, ncyc=Oasys.gRPC.defaultArg, fsplit=Oasys.gRPC.defaultArg, ndflag=Oasys.gRPC.defaultArg, cflag=Oasys.gRPC.defaultArg):
        handle = Oasys.PRIMER._connection.constructor(self.__class__.__name__, model, type, psid, nshv, ftype, ftensr, nthhsv, intstrn, optcard, sldo, ncyc, fsplit, ndflag, cflag)
        Oasys.gRPC.OasysItem.__init__(self, self.__class__.__name__, handle)
        """
        Create a new InterfaceSpringback object

        Parameters
        ----------
        model : Model
            Model that interface springback will be created in
        type : constant
            Specify the type of InterfaceSpringback (Can be
            InterfaceSpringback.NIKE3D or
            InterfaceSpringback.LSDYNA or
            InterfaceSpringback.NASTRAN or
            InterfaceSpringback.SEAMLESS )
        psid : integer
            Optional. Part set ID for springback
        nshv : integer
            Optional. Num additional Shell/Solid history variables number
        ftype : integer
            Optional. Filetype (0-3, 10-12)
        ftensr : integer
            Optional. Flag for dumping tensor data from the element history variables into the dynain file (0/1)
        nthhsv : integer
            Optional. Number of thermal history variables
        intstrn : integer
            Optional. Output of strains at all integration points of shell element is requested
        optcard : boolean
            Optional. Whether to have an optional card. Can be true or false
        sldo : integer
            Optional. Output of solid element data as 0 - \*ELEMENT_SOLID, 1- \*ELEM_SOLID_ORTHO.
            Used only for optional card
        ncyc : integer
            Optional. Number of process cycles. Used only for optional card
        fsplit : integer
            Optional. Flag for splitting of the dynain file (0 - One file, 1 - Two files.). Used only for optional card
        ndflag : integer
            Optional. Flag to dump nodes into dynain file
        cflag : integer
            Optional. Output contact state

        Returns
        -------
        dict
            InterfaceSpringback object
        """


# String representation
    def __repr__(self):
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "toString")


# Static methods
    def Create(model, modal=Oasys.gRPC.defaultArg):
        """
        Starts an interactive editing panel to create an InterfaceSpringback definition

        Parameters
        ----------
        model : Model
            Model that the InterfaceSpringback will be created in
        modal : boolean
            Optional. If this window is modal (blocks the user from doing anything else in PRIMER
            until this window is dismissed). If omitted the window will be modal

        Returns
        -------
        dict
            InterfaceSpringback object (or None if not made)
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "Create", model, modal)

    def First(model):
        """
        Returns the first interface springback in the model

        Parameters
        ----------
        model : Model
            Model to get first interface springback in

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object (or None if there are no interface springbacks in the model)
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "First", model)

    def FlagAll(model, flag):
        """
        Flags all of the interface springbacks in the model with a defined flag

        Parameters
        ----------
        model : Model
            Model that all interface springbacks will be flagged in
        flag : Flag
            Flag to set on the interface springbacks

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "FlagAll", model, flag)

    def GetAll(model):
        """
        Returns a list of InterfaceSpringback objects for all of the interface springbacks in a model in Primer

        Parameters
        ----------
        model : Model
            Model to get interface springbacks from

        Returns
        -------
        list
            List of InterfaceSpringback objects
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "GetAll", model)

    def GetFlagged(model, flag):
        """
        Returns a list of InterfaceSpringback objects for all of the flagged interface springbacks in a model in Primer

        Parameters
        ----------
        model : Model
            Model to get interface springbacks from
        flag : Flag
            Flag set on the interface springbacks that you want to retrieve

        Returns
        -------
        list
            List of InterfaceSpringback objects
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "GetFlagged", model, flag)

    def GetFromID(model, number):
        """
        Returns the InterfaceSpringback object for a interface springback ID

        Parameters
        ----------
        model : Model
            Model to find the interface springback in
        number : integer
            number of the interface springback you want the InterfaceSpringback object for

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object (or None if interface springback does not exist)
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "GetFromID", model, number)

    def Last(model):
        """
        Returns the last interface springback in the model

        Parameters
        ----------
        model : Model
            Model to get last interface springback in

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object (or None if there are no interface springbacks in the model)
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "Last", model)

    def Select(flag, prompt, limit=Oasys.gRPC.defaultArg, modal=Oasys.gRPC.defaultArg):
        """
        Allows the user to select interface springbacks using standard PRIMER object menus

        Parameters
        ----------
        flag : Flag
            Flag to use when selecting interface springbacks
        prompt : string
            Text to display as a prompt to the user
        limit : Model or Flag
            Optional. If the argument is a Model then only interface springbacks from that model can be selected.
            If the argument is a Flag then only interface springbacks that
            are flagged with limit can be selected (limit should be different to flag).
            If omitted, or None, any interface springbacks can be selected.
            from any model
        modal : boolean
            Optional. If selection is modal (blocks the user from doing anything else in PRIMER
            until this window is dismissed). If omitted the selection will be modal

        Returns
        -------
        int
            Number of interface springbacks selected or None if menu cancelled
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "Select", flag, prompt, limit, modal)

    def Total(model, exists=Oasys.gRPC.defaultArg):
        """
        Returns the total number of interface springbacks in the model

        Parameters
        ----------
        model : Model
            Model to get total for
        exists : boolean
            Optional. true if only existing interface springbacks should be counted. If false or omitted
            referenced but undefined interface springbacks will also be included in the total

        Returns
        -------
        int
            number of interface springbacks
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "Total", model, exists)

    def UnflagAll(model, flag):
        """
        Unsets a defined flag on all of the interface springbacks in the model

        Parameters
        ----------
        model : Model
            Model that the defined flag for all interface springbacks will be unset in
        flag : Flag
            Flag to unset on the interface springbacks

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.classMethod(__class__.__name__, "UnflagAll", model, flag)



# Instance methods
    def AssociateComment(self, comment):
        """
        Associates a comment with a interface springback

        Parameters
        ----------
        comment : Comment
            Comment that will be attached to the interface springback

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "AssociateComment", comment)

    def Browse(self, modal=Oasys.gRPC.defaultArg):
        """
        Starts an edit panel in Browse mode

        Parameters
        ----------
        modal : boolean
            Optional. If this window is modal (blocks the user from doing anything else in PRIMER
            until this window is dismissed). If omitted the window will be modal

        Returns
        -------
        None
            no return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Browse", modal)

    def ClearFlag(self, flag):
        """
        Clears a flag on the interface springback

        Parameters
        ----------
        flag : Flag
            Flag to clear on the interface springback

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "ClearFlag", flag)

    def Copy(self, range=Oasys.gRPC.defaultArg):
        """
        Copies the interface springback. The target include of the copied interface springback can be set using Options.copy_target_include

        Parameters
        ----------
        range : boolean
            Optional. If you want to keep the copied item in the range specified for the current include. Default value is false.
            To set current include, use Include.MakeCurrentLayer()

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Copy", range)

    def DetachComment(self, comment):
        """
        Detaches a comment from a interface springback

        Parameters
        ----------
        comment : Comment
            Comment that will be detached from the interface springback

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "DetachComment", comment)

    def Edit(self, modal=Oasys.gRPC.defaultArg):
        """
        Starts an interactive editing panel

        Parameters
        ----------
        modal : boolean
            Optional. If this window is modal (blocks the user from doing anything else in PRIMER
            until this window is dismissed). If omitted the window will be modal

        Returns
        -------
        None
            no return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Edit", modal)

    def Flagged(self, flag):
        """
        Checks if the interface springback is flagged or not

        Parameters
        ----------
        flag : Flag
            Flag to test on the interface springback

        Returns
        -------
        bool
            True if flagged, False if not
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Flagged", flag)

    def GetComments(self):
        """
        Extracts the comments associated to a interface springback

        Returns
        -------
        list
            List of Comment objects (or None if there are no comments associated to the node)
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "GetComments")

    def GetExcludeKeyword(self, idx):
        """
        Returns the keyword string excluded at given index in Keyword list. Needed only for InterfaceSpringback.EXCLUDE.

        Parameters
        ----------
        idx : integer
            The index in Keyword list you want the Keyword string for. Note that indices start at 0, not 1

        Returns
        -------
        str
            A Keyword string at index "idx" from excluded keyword list
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "GetExcludeKeyword", idx)

    def GetNodalPoint(self, npt):
        """
        Returns the data for nodal point constrained for \*INTERFACE_SPRINGBACK

        Parameters
        ----------
        npt : integer
            The nodal point you want the data for. Note that nodal points start at 0, not 1

        Returns
        -------
        list
            A list containing the Node id, translational constraint (TC) and rotational constraint (RC) constants
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "GetNodalPoint", npt)

    def GetParameter(self, prop):
        """
        Checks if a InterfaceSpringback property is a parameter or not.
        Note that object properties that are parameters are normally returned as the integer or
        float parameter values as that is virtually always what the user would want. For this function to
        work the JavaScript interpreter must use the parameter name instead of the value. This can be done by setting
        the Options.property_parameter_names option to true
        before calling the function and then resetting it to false afterwards..
        This behaviour can also temporarily be switched by using the InterfaceSpringback.ViewParameters()
        method and 'method chaining' (see the examples below)

        Parameters
        ----------
        prop : string
            interface springback property to get parameter for

        Returns
        -------
        dict
            Parameter object if property is a parameter, None if not
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "GetParameter", prop)

    def Keyword(self):
        """
        Returns the keyword for this Interface Springback (\*INTERFACE_SPRINGBACK_xxxx_xxxx)
        Note that a carriage return is not added.
        See also InterfaceSpringback.KeywordCards()

        Returns
        -------
        str
            string containing the keyword
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Keyword")

    def KeywordCards(self):
        """
        Returns the keyword cards for the InterfaceSpringback.
        Note that a carriage return is not added.
        See also InterfaceSpringback.Keyword()

        Returns
        -------
        str
            string containing the cards
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "KeywordCards")

    def Next(self):
        """
        Returns the next interface springback in the model

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object (or None if there are no more interface springbacks in the model)
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Next")

    def Previous(self):
        """
        Returns the previous interface springback in the model

        Returns
        -------
        InterfaceSpringback
            InterfaceSpringback object (or None if there are no more interface springbacks in the model)
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Previous")

    def RemoveExcludeKeyword(self, idx):
        """
        Removes the keyword string excluded at given index in Keyword list. Needed only for InterfaceSpringback.EXCLUDE

        Parameters
        ----------
        idx : integer
            The index in Keyword list you removed. Note that indices start at 0, not 1

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "RemoveExcludeKeyword", idx)

    def RemoveNodalPoint(self, npt):
        """
        Removes the nodal point for constrained node for \*INTERFACE_SPRINGBACK

        Parameters
        ----------
        npt : integer
            The nodal point you want to remove.
            Note that nodal points start at 0, not 1

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "RemoveNodalPoint", npt)

    def SetExcludeKeyword(self, keystr, index=Oasys.gRPC.defaultArg):
        """
        Sets a keyword string to be excluded. Adds a new keyword if index value is not given, else replaces the keyword string at given index. 
        Note that indices start at 0, not 1. Needed only for InterfaceSpringback.EXCLUDE

        Parameters
        ----------
        keystr : string
            The keyword string you want to be excluded
        index : integer
            Optional. The index at which keyword string should be set

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "SetExcludeKeyword", keystr, index)

    def SetFlag(self, flag):
        """
        Sets a flag on the interface springback

        Parameters
        ----------
        flag : Flag
            Flag to set on the interface springback

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "SetFlag", flag)

    def SetNodalPoint(self, npt, nid, tc, rc):
        """
        Sets the nodal point data for a node in \*INTERFACE_SPRINGBACK

        Parameters
        ----------
        npt : integer
            The nodal point you want to set the data for.
            Note that nodal points start at 0, not 1
        nid : integer
            Node ID for the nodal point
        tc : real
            Translational constraint constant of the nodal point. (0-7)
        rc : real
            Rotational constraint constant of the nodal point. (0-7)

        Returns
        -------
        None
            No return value
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "SetNodalPoint", npt, nid, tc, rc)

    def ViewParameters(self):
        """
        Object properties that are parameters are normally returned as the integer or
        float parameter values as that is virtually always what the user would want. This function temporarily
        changes the behaviour so that if a property is a parameter the parameter name is returned instead.
        This can be used with 'method chaining' (see the example below) to make sure a property argument is correct

        Returns
        -------
        dict
            InterfaceSpringback object
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "ViewParameters")

    def Xrefs(self):
        """
        Returns the cross references for this interface springback

        Returns
        -------
        dict
            Xrefs object
        """
        return Oasys.PRIMER._connection.instanceMethod(self.__class__.__name__, self._handle, "Xrefs")

